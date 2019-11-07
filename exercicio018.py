import math

angulo =  float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O seno é {:.2f}.\n O cosseno é {:.2f}.\n A tangente é {:.2f}.".format(seno,cosseno,tangente))


