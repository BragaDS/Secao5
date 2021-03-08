num1 = int(input("Digite o primeiro numero \n"))
num2 = int(input("Digite o segundo numero \n"))

if num1 > num2:
    dif = num1 - num2
    print(f"O {num1} é maior que o {num2} e a diferença é {dif}")
elif num1 < num2:
    dif = num2 - num1
    print(f"O {num2} é maior que o {num1} e a diferença é {dif}")
else:
    print("Os numeros são iguais")
