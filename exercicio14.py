not1 = float(input("Digite a nota do trabalho de laboratório \n"))
not2 = float(input("Digite a nota da avaliação semestral \n"))
not3 = float(input("Digite a nota do exame final \n"))

media = ((not1 * 2) + (not2 * 3) + (not3 * 5)) / 10

print(f"A média do aluno é de {media}")

if media < 3:
    print("REPROVADO")
elif 3 < media < 5:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
