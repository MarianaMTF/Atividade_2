ano=int(input("digite o ano de agora:"))
nome_1=input("digite o nome da primeira pessoa:")
idade_1=int(input("digite a idade da primeira pessoa:"))
nome_2=input("digite o nome da segunda pessoa:")
idade_2 = int(input("digite a idade da segunda pessoa::"))

if idade_1>idade_2:
    print(nome_2+" eh mais novo e nasceu em:"+str(ano-idade_2))
elif idade_1==idade_2:
    print(nome_1+"e "+nome_2+"tem a mesma idade e nasceram em:"+str(ano-idade_1))
else:
    print(nome_1+"eh mais novo e nasceu em:"+str(ano-idade_1))