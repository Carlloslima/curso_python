valor = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Pretende pagar em quantos anos: "))

vmensal = valor / (anos * 12)
perc_salar = salario * 0.30

if vmensal > perc_salar:
    print("Você não poderá comprar esse imóvel. Pois o valor mensal exede os 30% do seu salario.")
    print("\033[1;30;45m  Valor mensarl:\033[m R${:.2f}".format(vmensal))
    print("\033[7;30;45m Salario:\033[m R${:.2f}".format(salario))
    print("\033[1;35;43m Porcentagem:\033[m {}".format(perc_salar))
else:
    print("\033[1;30;45m O valor mensal do imóvel é de {:.2f} em {} anos.\033[m".format(vmensal, anos))