sal = float(input("Digite o seu salario: "))
meta = 1250.00

if sal > meta:
    val = sal * 0.10
    print("O seu aumento é de {:.2f}, ficando com salario de {:.2f}".format(val, sal + val))
else:
    val = sal * 0.15
    print("O seu aumento é de {:.2f}, ficando com o salario de {:.2f}".format(val, sal + val))