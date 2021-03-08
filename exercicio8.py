av1 = 0
av2 = 0

nota1 = float(input("Digita a nota da primeira avaliação \n"))
if 0 <= nota1 < 11:
    av1 = nota1
else:
    print("Nota invalida")
    exit()

nota2 = float(input("Digita a nota da segunda avaliação \n"))
if nota2 >= 0 and nota1 < 11:
    av2 = nota2
else:
    print("Nota invalida")
    exit(),

media = (av1 + av2) / 2
print(f"A média final do aluno é: {media} ")
