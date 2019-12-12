from datetime import date

ano = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano

if idade > 18:
    print("Você já passou da idade para se alistar.")
elif idade < 18:
    print("Você ainda não pode se alistar.")
else:
    print("Está é a hora de se alistar.")