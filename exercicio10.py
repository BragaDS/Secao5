sex = int(input("Digite seu sexo\n "
                "Digite 1 para homem \n "
                "Digite 2 para mulher \n"))

h = float(input("Digite sua altura \n"))

if sex == 1:
    pi = (72.7 * h) - 58
    print(f"O seu peso ideal é {pi}")
elif sex == 2:
    pi = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {pi}")
else:
    print("Você não digitou um código para sexo valido")
