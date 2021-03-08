diasemana = ['domingo',
             'segunda',
             'terça',
             'quarta',
             'quinta',
             'sexta',
             'sábado']

dia = int(input('Digite o dia da semana \n'))

if 1 < dia > 7:
    print('Esse dia não existe')
else:
    print(f'O dia selecionado é: {diasemana[dia - 1]}.')
