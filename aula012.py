nome = str(input("Digite seu nome: ")).strip()

if nome == "Carlos":
    print("Seu nomeé muito legal, {} !".format(nome))
elif  nome == "Pedro" or nome == "Paulo":
    print("Seu nome é biblico, {} ".format(nome))
elif nome in "Juca Jonas Jurema":
    print("Seu nome está la terceiro condição")
else:
    print("Você está no else")
