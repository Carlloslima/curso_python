km= float(input("Qual a quantidade de KM rodados? "))
dias= int(input("Qual a quantidade de dias que foi alugado? "))
diaria= dias * 60
kilometragem = km * 0.15

print("O valor total a pagar é R${:.2f} ".format(diaria + kilometragem))
print("Foi cobrado R${:.2f} pelos dias e R${:.2f} pelos KMs.".format(diaria, kilometragem))