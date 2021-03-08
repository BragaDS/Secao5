print("               Cardápio \n"
      "Especificação    | COD | Preço       \n"
      "Cachorro quente: | 100 | Valor: 1.20 \n"
      "Bauru Simples:   | 101 | Valor: 1.30 \n"
      "Bauru com Ovo:   | 102 | Valor: 1.50 \n"
      "Hamburguer:      | 103 | Valor: 1.20 \n"
      "Cheeseburguer:   | 104 | Valor: 1.70 \n"
      "Suco             | 105 | Valor: 2.20 \n"
      "Refrigerante     | 106 | Valor: 1.20 \n")

pre = {100: 1.20,
       101: 1.30,
       102: 1.50,
       103: 1.20,
       104: 1.70,
       105: 2.20,
       106: 1.20}

prod = {100: 'Cachorro quente',
        101: 'Bauru Simples',
        102: 'Bauru com Ovo',
        103: 'Hamburguer',
        104: 'Cheeseburguer',
        105: 'Suco',
        106: 'Refrigerante'}

cod = int(input("Digite o código do produto \n"))

while cod > 106 or cod < 100:
    print("Código invalido, digite o código novamente \n \n")
    print("               Cardápio \n"
          "Especificação    | COD | Preço       \n"
          "Cachorro quente: | 100 | Valor: 1.20 \n"
          "Bauru Simples:   | 101 | Valor: 1.30 \n"
          "Bauru com Ovo:   | 102 | Valor: 1.50 \n"
          "Hamburguer:      | 103 | Valor: 1.20 \n"
          "Cheeseburguer:   | 104 | Valor: 1.70 \n"
          "Suco             | 105 | Valor: 2.20 \n"
          "Refrigerante     | 106 | Valor: 1.20 \n")

    cod = int(input("Digite o código do produto \n"))

qtd = int(input(f"Digite a quantidade de {prod[cod]} \n"))
print(f"O valor a ser pago é R${qtd * pre[cod]:.2f}")

