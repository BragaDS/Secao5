sal = float(input("Digite o salário \n"))
prest = float(input("Digite o valor da prestação do empréstimo \n"))

if prest > (sal * 0.20):
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido")
