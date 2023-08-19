aco=int(input("digite a quantidade de aço: "))
cobre=int(input("digite a quantidade de cobre: "))
aluminio=int(input("digite a quantidade de aluminio: "))
total=(aco * 2.50)+(cobre * 4)+(aluminio * 4.50)

print("o total pra pagar: R$"+str(total))
haste_total=aco+cobre+aluminio

if haste_total<=6:
    print("desconto: 0" )
elif 7<=haste_total<=15:
    desconto=0.10
    total=total*(1-desconto)
    print("desconto:"+str(desconto))
    print("valor:"+str(total))
elif 16<=haste_total<=20:
    desconto=0.15
    total=total*(1-desconto)
    print("desconto:"+str(desconto))
    print("valor: "+str(total))
elif haste_total>20:
    desconto=0.20
    total=total*(1-desconto)
    print("desconto:"+str(desconto))
    print("valor:"+str(total))