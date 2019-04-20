# supports position

lR = [0, 0.5]

# Load declaration
# UDL

mlUDL = [[0, 0.5], [0.5, 0.75], [0.75, 2]]    # [start, end]
mUDL = [2, 2, 2]

# Forces

mlF = [1]
mF = [4]

# Momentums

mlM = []
mM = []

# Reactions componens declaration

UDLr1 = 0        # UDL component in R1 calculation
UDLr2 = 0        # UDL component in R2 calculation
Fr1 = 0         # F component in R1 calculation
Fr2 = 0         # F component in R2 calculation
Mr1 = 0
Mr2 = 0

for i in range(len(mUDL)):
    UDLr1temp = mUDL[i] * (mlUDL[i][1] - mlUDL[i][0]) * \
        (lR2 - (mlUDL[i][0] + ((mlUDL[i][1] - mlUDL[i][0]) / 2)))
    UDLr2temp = mUDL[i] * (mlUDL[i][1] - mlUDL[i][0]) * \
        (lR1 - (mlUDL[i][0] + ((mlUDL[i][1] - mlUDL[i][0]) / 2)))
    UDLr1 += UDLr1temp
    UDLr2 += UDLr2temp

for i in range(len(mF)):
    Fr1temp = mF[i] * (lR2 - mlF[i])
    Fr2temp = mF[i] * (lR1 - mlF[i])
    Fr1 += Fr1temp
    Fr2 += Fr2temp

for i in range(len(mM)):
    Mr1 += mM[i]
    Mr2 += mM[i]

R1 = (Fr1 + UDLr1 + Mr1) / (lR[1] - lR[0])
R2 = (Fr2 + UDLr2 + Mr2) / (lR[0] - lR[1])

print('R1 = ' + str(R1))
print('R2 = ' + str(R2))
