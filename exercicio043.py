peso = float(input("Peso: "))
altura = float(input("Altura: "))

peso_convertido = peso / 100

imc: float = peso_convertido

if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5 <= imc < 25:
    print("Peso ideal!")
elif 25 <= imc <= 30:
    print("Sobrepeso")
elif 30 < imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")
