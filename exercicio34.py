nota = float(input("Digite a nota do aluno \n"))
fal = int(input("Digite o numero de faltas do aluno \n"))

while nota > 10 or nota < 0:
    print("Nota invalida, digite uma nota de 0 a 10 \n")
    nota = float(input("Digite a nota do aluno \n"))

if 9 <= nota <= 10:
    if fal < 21:
        print("CONCEITO A")
    else:
        print("CONCEITO B")

elif 7.5 <= nota <= 8.9:
    if fal < 21:
        print("CONCEITO B")
    else:
        print("CONCEITO C")

elif 5 <= nota <= 7.4:
    if fal < 21:
        print("CONCEITO C")
    else:
        print("CONCEITO D")

elif 4 <= nota <= 4.9:
    if fal < 21:
        print("CONCEITO D")
    else:
        print("CONCEITO E")

else:
    print("CONCEITO E")

