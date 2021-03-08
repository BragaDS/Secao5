from random import randint
count = 0
cert = 0

while count < 5:
    count = count + 1
    num1 = randint(0, 99)
    num2 = randint(0, 99)
    aResp = int(input(f"Pergunta de numero {count}. \n "
                      f"Digite abaixo a soma de {num1} + {num2} \n"))
    resp = (num1 + num2)
    if aResp != resp:
        print(f"Você errou, a soma de {num1} + {num2} é: {resp} \n")
        print(f"Você tem {cert} acertos")
    else:
        print(f"Você acertou! A soma de {num1} + {num2} é: {aResp} \n")
        cert = cert + 1
        print(f"Você tem {cert} acertos \n")
