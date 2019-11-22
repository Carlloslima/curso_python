ano = int(input("Digite um ano: "))
criterio1 = ano % 4   #Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
criterio2 = ano % 100 #Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
criterio3 = ano % 400 #Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.


if criterio1 == 0 and criterio2 != 0 :
    print("O ano digitado é bissexto!!")
else:
    print("O ano digitado não é bissexto!")