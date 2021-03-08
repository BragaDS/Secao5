import math

num = int(input(f"Digite um numero \n"))

if num <= 0:
    print(f"O numero {num} é invalido")
else:
    rqd = math.sqrt(num)
    print(f"A raiz quadradada de {num} é {rqd}")
