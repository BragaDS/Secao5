valor_fabrica = float(input("Digite aqui o valor do carro de fábrica: \n"))

if valor_fabrica <= 12000:
    valor_fabrica = valor_fabrica * 1.05
    print(f"O valor do carro após o calculo de imposto é {valor_fabrica:.2f}")

elif 25000 >= valor_fabrica > 12000:
    valor_final = (valor_fabrica * 1.10) + (valor_fabrica * 0.15)
    print(f"O valor do carro após o calculo de imposto é {valor_final:.2f}")

elif 25000 < valor_fabrica:
    valor_final = (valor_fabrica * 1.15) + (valor_fabrica * 0.20)
    print(f"O valor do carro após o calculo de imposto é {valor_final:.2f}")
