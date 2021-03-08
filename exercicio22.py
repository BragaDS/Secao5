ida = int(input("Digite sua idade \n"))
temp = int(input("Digite a quantidade de anos de contribuição \n"))

if ida >= 65:
    print("Você pode se aposentar por ter mais de 64 anos")
elif temp > 29:
    print("Você pode se aposentar por ter trabalhado mais de 29 anos")
elif 65 > ida >= 60 and temp > 24:
    print("Você pode se aposentar por ter mais 24 anos de trabalho e a idade minima de 60 anos")
else:
    print("Você não atende os requisitos de aposentadoria")
