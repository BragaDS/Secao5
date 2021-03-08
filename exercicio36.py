men = float(input("Digite o valor de vendas mensal \n"))

if men >= 100000:
    com = 700 + (men * 0.16)
    print(f"O valor da comissão é: R${com:.2f}")
elif 100000 > men >= 60000:
    com = 650 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")
elif 80000 > men >= 60000:
    com = 600 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")
elif 60000 > men >= 40000:
    com = 550 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")
elif 40000 > men >= 20000:
    com = 500 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")
else:
    com = 400 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")