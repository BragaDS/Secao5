import math

numR = float(input("Digite um numero real \n"))

if numR >= 0:
    rqd = math.sqrt(numR)
    print(f"A raiz quadrada é {rqd}")
else:
    nqd = numR ** 2
    print(f"O numero digitado ao quadrado é: {nqd}")
