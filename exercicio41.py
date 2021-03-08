altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Abaixo do peso")
elif 25 > imc > 18.5:
    print("Saudável")
elif 30 > imc >= 25:
    print("Peso em excesso")
elif 35 > imc >= 30:
    print("Obesidade grau 1")
elif 40 > imc >= 35:
    print("Obesidade grau 2 (severa)")
else:
    print("Obesidade grau 3 (morbida)")
