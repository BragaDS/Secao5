a = int(input("Digite o lado A de um triangulo \n"))
b = int(input("Digite o lado B de um triangulo \n"))
c = int(input("Digite o lado C de um triangulo \n"))

while b + c < a:
    print("O valor inserido em 'A' não pode ser maior que a soma de 'B' + 'C', digite novamente")
    a = int(input("Digite o lado A de um triangulo \n"))
    b = int(input("Digite o lado B de um triangulo \n"))
    c = int(input("Digite o lado C de um triangulo \n"))

while a + c < b:
    print("O valor inserido em 'B' não pode ser maior que a soma de 'A' + 'C', digite novamente")
    a = int(input("Digite o lado A de um triangulo \n"))
    b = int(input("Digite o lado B de um triangulo \n"))
    c = int(input("Digite o lado C de um triangulo \n"))

while a + b < c:
    print("O valor inserido em 'C' não pode ser maior que a soma de 'A' + 'B', digite novamente")
    a = int(input("Digite o lado A de um triangulo \n"))
    b = int(input("Digite o lado B de um triangulo \n"))
    c = int(input("Digite o lado C de um triangulo \n"))

if a == b == c:
    print("O triangulo é equilatero")
elif a == b != c or a == c != b or c == b != a:
    print("O triangulo é isosceles")
else:
    print("O triangulo é escaleno")
