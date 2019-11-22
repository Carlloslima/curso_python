vel = int(input("Digite a velocidade do carro aqui: "))
media=80

if vel > media:
    print("Carro multado por excesso de velocidade.")
    print("Velocidade {}".format(vel))
    multa = (vel - media) * 7
    print("Multa de {} reais".format(multa))
