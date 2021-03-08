data = input('Informe uma data dd/mm/yyyy: ')

dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
valida = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        valida = 1
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= dia <= 30:
        valida = 1
elif mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        if dia <= 29:
            valida = 1
    elif dia <= 28:
        valida = 1

if valida == 1:
    print(f'A data {data} é válida')
else:
    print(f'A data {data} é invalida')
