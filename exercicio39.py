salario_atual = float(input("Informe o salário atual do funcionário \n"))
tempo_de_servico = int(input("Informe em meses o tempo de trabalho do funcionário na empresa \n"))
tempo_de_servico = tempo_de_servico / 12

if salario_atual <= 500:
    salario_atual = salario_atual * 1.25
elif salario_atual <= 1000:
    salario_atual = salario_atual * 1.20
elif salario_atual <= 1500:
    salario_atual = salario_atual * 1.15
elif salario_atual <= 2000:
    salario_atual = salario_atual * 1.10

if 0 < tempo_de_servico < 4:
    salario_atual = salario_atual + 100
elif 3 < tempo_de_servico < 7:
    salario_atual = salario_atual + 200
elif 6 < tempo_de_servico < 11:
    salario_atual = salario_atual + 300
elif tempo_de_servico > 10:
    salario_atual = salario_atual + 500

print(f"O salário atual do funcionário é: {salario_atual}")
