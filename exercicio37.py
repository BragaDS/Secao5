cheg = str(input("Digite a hora de chegada \n"))
said = str(input("Digite a hora de saida \n"))

hor, minu = cheg.split(":")
sHor, sMinu = said.split(":")

hor = int(hor)
minu = int(minu)
sHor = int(sHor)
sMinu = int(sMinu)
temM = 0
temH = 0

if hor < sHor:
    temH = (sHor - hor)
    if minu < sMinu:
        temH = temH + 1

elif hor > sHor:
    temH = 24 - (hor - sHor)
    if minu < sMinu:
        temH = temH + 1

elif hor == sHor and minu > sMinu:
    temH = 24

elif hor == sHor and minu == sMinu:
    temH = 1

elif hor == sHor and minu < sMinu:
    temH = 1

if temH < 3:
    print(f"O valor cobrador será de R${temH * 1:.2f}")
elif 2 < temH < 5:
    print(f"O valor cobrador será de R${(2 * 1) + ((temH - 2) * 1.4):.2f}")
else:
    print(f"O valor cobrador será de R${((2 * 1) + (2 * 1.4)) + ((temH - 4) * 2):.2f}")
