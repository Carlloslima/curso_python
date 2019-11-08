n = str(input("Digite seu nome completo ")).strip()
lista=n.split()
fim = len(lista)
print("Seu primeiro nome é {} e o último é {}".format(lista[0], lista[fim -1]))
