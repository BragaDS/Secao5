print("Escolha a operação matemática abaixo")
opc = 0

while 1 > opc or opc > 4:
    opc = int(input("1. Para soma digite 1 \n"
                    "2. Para Subtração digite 2 \n"
                    "3. Para multiplicação digite 3 \n"
                    "4. Para divisão digite 4 \n"))

val1 = int(input("Digite o primeiro valor da operação \n"))
val2 = int(input("Digite o segundo valor da operação \n"))

if opc == 1:
    result = val1 + val2
    print(f"O resultado é: {result}")
elif opc == 2:
    result = val1 - val2
    print(f"O resultado é: {result}")
elif opc == 3:
    result = val1 * val2
    print(f"O resultado é: {result}")
elif opc == 4:
    result = val1 / val2
    print(f"O resultado é: {result}")
else:
    print("O Numero digitado é invalido")
