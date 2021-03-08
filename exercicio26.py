km = int(input("Digite a quantidade de KMs percorrida \n"))
lit = int(input("Digite a quantidade de litros utilizada \n"))
cons = km / lit

if cons < 8:
    print("VENDA O CARRO")
elif 7 < cons < 12:
    print("ECONOMICO")
else:
    print("SUPER ECONOMICO")
