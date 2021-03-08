ida = int(input("Digite a idade do nadador \n"))
while ida < 5:
    print("Idade não permitida, somente acima de 5 anos \n")
    ida = int(input("Digite a idade do nadador \n"))

if 8 > ida > 4:
    print("O Nadador está classificado na categoria Infantil A")
elif 11 > ida > 7:
    print("O Nadador está classificado na categoria Infantil B")
elif 14 > ida > 10:
    print("O Nadador está classificado na categoria Juvenil A")
elif 18 > ida > 13:
    print("O Nadador está classificado na categoria Juvenil B")
else:
    print("O Nadador está classificado na categoria Senior")
