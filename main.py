# Reaction calculator - staticaly determined

L = 1
lR1 = 0
lR2 = 1
lF1 = 1
F1 = 4
lUDL = [0, 2]
UDL = 2

R1 = (F1*(lR2-lF1) + UDL*(lUDL[1]-lUDL[0])*(lR2-(lUDL[0]+((lUDL[1]-lUDL[0])/2))))/(lR2-lR1)
R2 = (F1*(lR1-lF1)+UDL*(lUDL[1]-lUDL[0])*(lR1-(lUDL[0]+((lUDL[1]-lUDL[0])/2))))/(lR1-lR2)

print('R1 = ' + str(R1))
print('R2 = ' + str(R2))

#calculating resultant momentum from UDLs

mlUDL = [[0, 0.5], [0.5, 0.75], [0.75, 2]]      #[start, end]
mUDL = [2, 2, 2]
nUDLr1 = 0
nUDLr2 = 0
for i in range(len(mUDL)):
    UDLr1temp = mUDL[i]*(mlUDL[i][1]-mlUDL[i][0])*(lR2-(mlUDL[i][0]+((mlUDL[i][1]-mlUDL[i][0])/2)))
    UDLr2temp = mUDL[i]*(mlUDL[i][1]-mlUDL[i][0])*(lR1-(mlUDL[i][0]+((mlUDL[i][1]-mlUDL[i][0])/2)))
    nUDLr1 += UDLr1temp
    nUDLr2 += UDLr2temp

R1 = (F1*(lR2-lF1) + nUDLr1)/(lR2-lR1)
R2 = (F1*(lR1-lF1) + nUDLr2)/(lR1-lR2)

print('R1 = ' + str(R1))
print('R2 = ' + str(R2))
