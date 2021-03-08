meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Maio',
         'Junho',
         'Julho',
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

mes = int(input('Digite o mês desejado \n'))

if 1 < mes > 12:
    print('Esse mês não existe')
else:
    print(f'O dia selecionado é: {meses[mes - 1]}.')
