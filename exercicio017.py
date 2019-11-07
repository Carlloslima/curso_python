import math
oposto = float(input("Digite o cateto oposto: "))
adjacente = float(input("Digite o cateto adjacente: "))
hi = (oposto**2 + adjacente**2)**(1/2)
hi2= math.hypot(oposto,adjacente)
print("A hipotenusa vai medir {} / {}".format(hi, hi2))

