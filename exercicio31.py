alt = float(input("Digite a sua altura \n"))
pes = float(input("Digite o seu peso \n"))

if alt < 1.20:
    if pes < 61:
         print("A classificação dessa pessoa é 'A'")
    elif 60 < pes < 90:
        print("A classificação dessa pessoa é 'B'")
    else:
         print("A classificação dessa pessoa é 'G'")

if 1.71 > alt > 1.19:
    if pes < 61:
         print("A classificação dessa pessoa é 'B'")
    elif 60 < pes < 90:
        print("A classificação dessa pessoa é 'E'")
    else:
         print("A classificação dessa pessoa é 'H'")

else:
    if pes < 61:
         print("A classificação dessa pessoa é 'C'")
    elif 60 < pes < 90:
        print("A classificação dessa pessoa é 'F'")
    else:
         print("A classificação dessa pessoa é 'I'")