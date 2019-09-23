import itertools as it
from sympy import Symbol, lambdify, Piecewise
from sympy.plotting import plot

x = Symbol('x')

'''
l - location
m - magnitude
'''
# supports position
lR = [0, 4]

# Load declaration
# UDL
lUDL = [[0, 3]]  # [start, end]
mUDL = [-1]

# Forces
lF = [0]
mF = [-3.45]

# Moments
lM = [2]
mM = [-1]

# Reactions components declaration
UDLr1 = 0  # UDL component in R1 calculation
UDLr2 = 0  # UDL component in R2 calculation
Fr1 = 0  # F component in R1 calculation
Fr2 = 0  # F component in R2 calculation
Mr1 = 0
Mr2 = 0

for i in range(len(mUDL)):
    UDLr1 -= mUDL[i] * (lUDL[i][1] - lUDL[i][0]) * \
             (lR[1] - (lUDL[i][0] + ((lUDL[i][1] - lUDL[i][0]) / 2)))
    UDLr2 -= mUDL[i] * (lUDL[i][1] - lUDL[i][0]) * \
             (lR[0] - (lUDL[i][0] + ((lUDL[i][1] - lUDL[i][0]) / 2)))

for i in range(len(mF)):
    Fr1 -= mF[i] * (lR[1] - lF[i])
    Fr2 -= mF[i] * (lR[0] - lF[i])

for i in range(len(mM)):
    Mr1 -= mM[i]
    Mr2 -= mM[i]

# Reactions calculation
R1 = (Fr1 + UDLr1 + Mr1) / (lR[1] - lR[0])
R2 = (Fr2 + UDLr2 + Mr2) / (lR[0] - lR[1])

print('R1 = ' + str(round(R1, 2)))
print('R2 = ' + str(round(R2, 2)))

# section of the beam
sections = []
for (s, u, f, m) in it.zip_longest(lR, lUDL, lF, lM, fillvalue='-'):
    for l in u:
        sections.append(l)
    sections.append(s)
    sections.append(f)
    sections.append(m)

sections = list(set(list(filter(lambda a: a != '-', sections))))
print(sections)


# Shear Force calculation


def shearForce(lowerB, upperB):
    global sf
    sf = 0
    for i in range(len(lUDL)):
        if lUDL[i][1] >= upperB:
            sf += mUDL[i] * (x - lUDL[i][0])

        elif lUDL[i][1] < upperB:
            sf += mUDL[i] * (lUDL[i][1] - lUDL[i][0])
    if lowerB >= lR[0]:
        sf += R1
    for i in range(len(mF)):
        if lowerB >= lF[i]:
            sf += mF[i]

    global f
    f = lambdify(x, sf)
    return f


# Bending Moment calculation

def bendingMoment(lowerB, upperB):
    global bm
    bm = 0
    for i in range(len(mUDL)):
        if lUDL[i][1] >= upperB:
            bm += mUDL[i] * ((x - lUDL[i][0]) ** 2) / 2
        elif lUDL[i][1] < upperB:
            bm += mUDL[i] * (lUDL[i][1] - lUDL[i][0]) * (x - ((lUDL[i][1] - lUDL[i][0]) / 2))
    if lowerB >= lR[0]:
        bm += R1 * (x - lR[0])
    for i in range(len(mF)):
        if lowerB >= lF[i]:
            bm += mF[i] * (x - lF[i])
    for i in range(len(mM)):
        if lowerB >= lM[i]:
            bm += mM[i]

    global b
    b = lambdify(x, bm)
    return b


sfFunc = {}
bmFunc = {}
for i in range(len(sections) - 1):
    lowerB = sections[i]
    upperB = sections[i + 1]
    shearForce(lowerB, upperB)
    bendingMoment(lowerB, upperB)
    sfFunc['f{0}'.format(i + 1)] = sf
    bmFunc['f{0}'.format(i + 1)] = bm
    print("for x = " + str(lowerB) + " SF = " + str(round(f(lowerB), 2)))
    print("for x = " + str(upperB) + " SF = " + str(round(f(upperB), 2)))
    print("for x = " + str(lowerB) + " BM = " + str(round(b(lowerB), 2)))
    print("for x = " + str(upperB) + " BM = " + str(round(b(upperB), 2)))
    print()

print(sfFunc)
print(bmFunc)

sfPlot = Piecewise((sfFunc['f1'], x <= sections[1]), (sfFunc['f2'], x <= sections[2]), (sfFunc['f3'], x <= sections[3]))

bmPlot = Piecewise((bmFunc['f1'], x <= sections[1]), (bmFunc['f2'], x <= sections[2]), (bmFunc['f3'], x <= sections[3]))
plot(sfPlot, bmPlot, (x, 0, 4))

