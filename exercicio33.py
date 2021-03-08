prod = float(input("Digite o valor do produto \n"))

if prod < 51:
    prod = prod * 1.05
elif 50 < prod < 100:
    prod = prod * 1.10
else:
    prod = prod * 1.15

print(f"O valor do produto atualizado é {prod:.2f}")

if prod < 81:
    print("BARATO")
elif 80 < prod < 121:
    print("NORMAL")
elif 120 < prod < 200:
    print("CARO")
else:
    print("MUITO CARO.")
