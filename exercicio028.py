import random
lista =[1,2,3,4,5]
computador1 = random.choice(lista)
computador= random.randint(0,5)
print("PC pensa {}".format(computador))
num = int(input("Escolha um número de 1 a 5: "))

if num == computador:
    print("Acertou Miseravel!")
else:
    print("Errou Miseravel!")
