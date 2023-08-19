sexo=input("digite qual eh seu sexo:")
peso=float(input("digite seu peso:"))
altura=float(input("digite sua altura:"))
idade = int(input("digite sua idade:"))

if sexo=="maculino":
    homem=66+(13.7*peso)+(5*altura)-(6.8 * idade)
    print("o recomendavel de caloria eh:"+str(homem)+" calorias")
elif sexo=="feminino":
    mulher=665+(9.6*peso)+(1.8*altura)-(4.7*idade)
    print("o recomendavel de caloria eh:"+str(mulher) +" calorias")