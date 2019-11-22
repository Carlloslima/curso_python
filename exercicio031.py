km = int(input("Digite a distancia da sua viagem em KM : "))
media= 200
preço1= 0.50
preço2= 0.45

if km <= media:
    print("O valor da sua viagem é de {} reias.".format(km * preço1))
else:
    print("O valor da sua viagem é de {} reias.".format(km * preço2))