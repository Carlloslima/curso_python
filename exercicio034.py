sal = float(input("Digite o seu salario: "))
meta = 1250.00

if sal > meta:
    val = sal * 0.1
    print("O seu aumento é de {}, ficando com salario de {}".format(val, sal + val))
else:
    val = sal * 0.15
    print("O seu aumento é de {}, ficando com o salario de {}".format(val, sal + val))