x = int(input("Leia o numero 'X' \n"))
y = int(input("Leia o numero 'Y' \n"))
z = int(input("Leia o numero 'Z' \n"))

med = (int(input("Digite a média desejada \n"
                 "Para Geométrica digite 1 \n"
                 "Para Ponderada digite 2 \n"
                 "Para Harmònica digite 3 \n"
                 "Para Aritmética digite 4 \n")))

while 4 < med or med < 1:
    print("Opção invalidade, digite novamente \n")
    med = int((input("Digite a média desejada \n"
                     "Para Geométrica digite 1 \n"
                     "Para Ponderada digite 2 \n"
                     "Para Harmònica digite 3 \n"
                     "Para Aritmética digite 4 \n")))

if med == 1:
    print(f"A média Geométrica dos valores escolhidos é: {(x * y * z) ** (1 / 3)}")
elif med == 2:
    print(f"A média Ponderada dos valores escolhidos é: {(x + 2 * y + 3 * z) / 6}")
elif med == 3:
    print(f"A média Harmônica dos valores escolhidos é: {1 / ((1 / x) + (1 / y) + (1 / z))}")
else:
    print(f"A média Aritmética dos valores escolhidos é: {(x + y + z) / 3}")
