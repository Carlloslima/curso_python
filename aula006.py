# int, floar, bool, str
# isnumeric(), isalnum(), isalpha(), isupper()
n1= int(input('Digite um numero?'))
n2= int(input('Digite um numero?'))
s=n1+n2
print(type(n1))
print('A soma entre ', n1, 'e ', n2, 'é: ',s)
print("A soma entre {} e {} é igual a: {}".format(n1, n2, s))
n= input('Digite um numero?')
print(n.isupper())
print(n1.isnumeric())


