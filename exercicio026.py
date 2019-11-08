n = str(input("Digite uma frase")).strip()

print("Quantas vezes o 'A' aparece? {}".format(n.upper().count('A')))
print("Qual a primeira vez? Posição {}".format(n.upper().find('A')+1))
print("E a ultima vez? Posição {}".format(n.upper().rfind('A')+1))