angulo1=int(input("digite o primeiro angulo:"))
angulo2=int(input("digite o segundo angulo:"))
angulo3=int(input("digite o terceiro angulo:"))

if angulo1<90 and angulo2<90 and angulo3<90:
    print("a figura eh um acutangulo")
elif angulo1==90 or angulo2==90 or angulo3==90:
    print("a figura eh um retângulo")
elif angulo1>90 or angulo2>90 or angulo3>90:
    print("a figura eh um obtusangulo")