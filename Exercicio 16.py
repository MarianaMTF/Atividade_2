numero = int(input("digite um numero de três digitos: "))

if 100<=numero<=999:
    digito_c=numero//100
    digito_d=numero%100
    digito_d=digito_d//10
    digito_u=numero%10
    soma=digito_c+digito_d+digito_u
    
    print("a soma dos digios:"+str(soma))
    if soma%16==0 and soma%4==0:
        print("a soma dos digitos eh divisivel por 16 e multiplo de 4")
    else:
        print("a soma dos digitos nao eh divisivel por 16 e multiplo de 4")
else:
    print("O dado nao esta valido")