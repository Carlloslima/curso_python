import random

n1 = input("Nome:")
n2 = input("Nome:")
n3 = input("Nome:")
n4 = input("Nome:")

escolha = random.choice([n1,n2,n3,n4])

print("Aluno escolhido é {}".format(escolha))
