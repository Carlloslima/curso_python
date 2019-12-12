n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um ultimo número: "))


if n1 > n2 :
    if n1 > n3:
        if n3 > n2:
            print("O primeiro número é o maior. N: {}".format(n1))
            print("O segundo é o menor. N {}".format(n2))
        else:
            print("O primeiro número é o maior. N: {}".format(n1))
            print("O terceiro número é o menor. N: {}".format(n3))
    else:
        print("O terceiro número é o maior, N: {}".format(n3))
        print("O segundo númer é o menor. N: {}".format(n2))
else:
    if n2 > n3:
        if n3 > n1:
            print("O segundo número é o maior. N {}".format(n2))
            print("O primeiro número é o menor. N: {}".format(n1))
        else:
            print("O segundo número é o maior. N {}".format(n2))
            print("O terceiro número é o menor. N: {}".format(n3))
    else:
        print("O terceiro número é o maior: N {}".format(n3))
        print("O primeiro número é o menor. N  {}".format(n1))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3

print("O menor número é {}".format(menor))
print("O maior número é {}".format(maior))