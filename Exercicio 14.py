consumidor=input("digite o tipo de consumidor(i, c, r)):")
consumo=float(input("digite o consumo:"))

if consumidor=="i":
    valor=(0.68*consumo)+34
    print("valor: R$"+str(valor))
elif consumidor=="c":
    valor=(0.37*consumo)+45
    print("valor: R$"+str(valor))
elif consumidor=="r":
    valor=(0.77*consumo)-22
    print("valor: R$"+str(valor))