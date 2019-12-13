r1 = float(input("Valor da reta 1: "))
r2 = float(input("Valor da reta 2: "))
r3 = float(input("Valor da reta 3: "))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
   if r1 == r2 and r2 == r3:
        print("Equilatero")
   elif (r1 == r2 or r2 == r3) and (r1 != r2 or r2 != r3):
       print("Isosceles")
   elif r1 != r2 and r2 != r3 and r1 != r3:
       print("Escaleno")
else:
    print("Não formam um triangulo.")