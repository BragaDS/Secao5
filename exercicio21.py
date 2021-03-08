opc = 0
result = 0
while opc > 4 or opc < 1:
    opc = int(input("Escolha uma das opções abaixo.\n "
                    "1. Para soma \n "
                    "2. para subtração \n "
                    "3. para multiplicação \n "
                    "4. para divisão \n"))
    if opc > 4 or opc < 1:
        print("Opção invalida, digite novamente \n")

a = int(input("Digite o numero A \n"))
b = int(input("Digite o numero B \n"))

if opc == 1:
    result = a + b

elif opc == 2:
    if a < b:
        result = b - a
    else:
        result = a - b

elif opc == 3:
    result = a * b

elif opc == 4:
    while b == 0:
        b = int(input("O B não pode ser 0, digite o B novamente \n"))
    result = a / b

print(f"O resultado esperado é: {result}")
