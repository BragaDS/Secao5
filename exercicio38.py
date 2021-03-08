data_de_nascimento = input("Digite aqui sua data de nascimento separada por barra, no padrão dd/mm/aaaa: \n")
data_sem_barra = data_de_nascimento.split("/")

# VALIDAÇÃO DA DATA DIGITADA
while len(data_sem_barra) != 3:
    print("Você digitou em um formato ERRADO, digite novamente \n")
    data_de_nascimento = input("Digite aqui sua data de nascimento separada por barra, no padrão dd/mm/aaaa: \n")
    data_sem_barra = data_de_nascimento.split("/")

dia = int(data_sem_barra[0])
mes = int(data_sem_barra[1])
ano = int(data_sem_barra[2])

# VALIDAÇÃO BISSEXTO
bissexto = 0
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    bissexto = 1

# VALIDAÇÃO ANO
if ano > 2021:
    print("DATA INVALIDA")
    exit()

# FEVEREIRO BISSEXTO
if mes == 2 and bissexto == 1 and 0 < dia < 30:
    print("DATA VÁLIDA")
# FEVEREIRO NÃO BISSEXTO
elif mes == 2 and bissexto == 0 and 0 < dia < 29:
    print("DATA VÁLIDA")

# MESES RESTANTES
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and 0 < dia < 32:
    print("DATA VÁLIDA")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and 0 < dia < 31:
    print("DATA VÁLIDA")

else:
    print("DATA INVALIDA")
