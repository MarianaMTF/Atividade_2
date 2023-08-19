salario_bruto=float(input("digite o salario bruto:"))

if salario_bruto<=1903.98:
    print("desconto:ISENTO")
    print("salario liquido:"+str(salario_bruto))
elif 1903.98<salario_bruto<=2826.65:
    imposto=0.075
    deducao=142.80
    imposto=(salario_bruto*imposto)-deducao
    print("desconto:"+str(imposto))
    print("salario liquido:"+str(salario_bruto-imposto))
elif 2826.65<salario_bruto<=3751.05:
    imposto=0.15
    deducao=548.82
    imposto=(salario_bruto*imposto)-deducao
    print("desconto:"+str(imposto))
    print("salario liquido:"+str(salario_bruto-imposto))
elif 3751.05<salario_bruto<=4664.68:
    imposto=0.225
    deducao=636.13
    imposto=(salario_bruto*imposto)-deducao
    print("desconto:"+str(imposto))
    print("salario liquido:" +str(salario_bruto-imposto))
elif salario_bruto>4664.68:
    imposto=0.275
    deducao=869.36
    imposto=(salario_bruto*imposto)-deducao
    print("desconto:"+str(imposto))
    print("salario liquido:"+str(salario_bruto-imposto))