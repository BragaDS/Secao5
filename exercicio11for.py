num = int(input("Digite um numero \n"))
soma = 0

if num >= 0:
    for i in str(num):
        soma = int(i) + soma
    print(soma)
else:
    print("Numero menor que 0")
