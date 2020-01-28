n = int(input("Digite um numero: "))
b = str(input("Qual base de conversão? ")).strip().upper()

if b == "BINARIO":
    print('{} convertido para BINARIO é igusl a {}.'.format(n, bin(n)[2:]))
elif b == "OCTAL":
    print("{} convertido para Octal é igual a {}.".format(n, oct(n)[2:]))
elif b == "HEXADECIMAL":
    print("{} convertido para Hexa é igual a {}.".format(n, hex(n)[2:]))
print("Opcao invalida, tente novamente.")