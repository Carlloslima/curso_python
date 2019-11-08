nome =  str(input("Digite o nome completo: ")).strip()

print("Nome completo maiúscula {}".format(nome.upper()))
print("Nome completo minuscula {}".format(nome.lower()))
print("Quantidade de letras ao todo {}".format(len(nome.replace(' ',''))))
print("Quantidade de letras ao todo {}".format(len(nome) - nome.count(' ')))
lista = nome.split()
print("Qtd letra primeiro nome {}".format(len(lista[0])))
print("Qtd letra primeiro nome {}".format(nome.find(' ')))