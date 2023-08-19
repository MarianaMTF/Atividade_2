numero_1=int(input("digite o primeiro numero:"))
numero_2=int(input("digite o segundo numero:"))
numero_3=int(input("digite o terceiro numero:"))

if numero_1>numero_2 and numero_1>numero_3:
    print("o numero "+str(numero_1)+" eh o maior")
elif numero_2>numero_1 and numero_2>numero_3:
    print("o numero "+str(numero_2) +" eh o maior")
else:
    print("o numero "+str(numero_3)+" eh o maior")