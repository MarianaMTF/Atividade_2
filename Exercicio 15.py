hora_i=int(input("digite a hora inicial:"))
minuto_i=int(input("digite o minuto inicial:"))
hora_f=int(input("digite a hora final:"))
minuto_f=int(input("digite o minuto final:"))

if hora_i<=23 and hora_f<=23:
    if minuto_i<=59 and minuto_f<=59:
        minutos_total=((hora_f*60)+minuto_f)-((hora_i*60)+minuto_i)
        horas=minutos_total//60
        minutos_total=minutos_total%60
        if horas<0:
            horas=-1*horas
            horas=24-horas
        if minutos_total==0:
            print("você jogou "+str(horas)+" horas")
        else:
            print("você jogou "+str(horas)+" horas e " +str(minutos_total)+" minutos")
    else:
        print("entrada de dados nao valida!")
else:
    print("entrada de dados nao valida!")