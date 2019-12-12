r1 = float(input("Valor da reta 1: "))
r2 = float(input("Valor da reta 2: "))
r3 = float(input("Valor da reta 3: "))


if (r2-r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
        print("As retas formam um triangulo")
else:
    print("Não formam um triangulo.")

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print("As retas formam um triangulo")
else:
    print("Não formam um triangulo.")