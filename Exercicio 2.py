d_carro_1=float(input("digite a distancia percorrida do primeiro carro:"))
t_carro_1=int(input("digite o tempo percorrido do primeiro carro:"))
d_carro_2=float(input("digite a distancia percorrida do segundo carro:"))
t_carro_2=int(input("digite o tempo percorrido do segundo carro:"))
vel_media_1=d_carro_1/t_carro_1
vel_media_2=d_carro_2/t_carro_2

if vel_media_1>vel_media_2:
    print("o primeiro carro tem velocidade maior que o segundo carro:"+str(vel_media_1)+" m/s")
elif vel_media_2>vel_media_1:
    print("o segundo carro tem velocidade maior que o primeiro carro:"+str(vel_media_2)+" m/s")
elif vel_media_1==vel_media_2:
    print("O primeiro carro e o segundo carro tem a mesma velocidade:"+str(vel_media_1)+" m/s")