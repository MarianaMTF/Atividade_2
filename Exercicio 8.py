d_percorrida=float(input("digite a distancia:"))
consumo=float(input("digite o quanto o carro consumiu:"))
consumo=d_percorrida/consumo

if consumo<8:
    print("venda o carro!")
elif consumo==8 or consumo<=14:
    print("economico!")
elif consumo>12:
    print("super economico!")