import random

n1 = input("Nome: ")
n2 = input("Nome: ")
n3 = input("Nome: ")
n4 = input("Nome: ")

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print("O primeiro aluno a se apresentar é {}, o segundo {}, depois {} e por ultimo {}.".format(lista[0],lista[1],lista[2],lista[3]))


