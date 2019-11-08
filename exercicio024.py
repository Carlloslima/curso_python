n = str(input("Digite o nome de uma cidade: ")).strip()

lista = n.split()
print("Essa cidade começa com 'SANTOS'? {}".format('SANTOS' in lista[0].upper()))
print(n[:6].upper() == 'SANTOS')
print("Essa cidade comeca com 'SANTOS'? {} ".format(n.upper().find('SANTOS')))