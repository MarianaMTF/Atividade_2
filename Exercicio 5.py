nome=input("digite seu nome:")
nota_1=float(input("digite sua primeira nota:"))
nota_2=float(input("digite sua segunda nota:"))
media=nota_1+nota_2/2

if media==0 or media<5:
    print("você foi reprovado")
elif media==5 or media<7:
    print("você esta de recuperação")
elif media==7 or media<=10:
    print("você foi aprovado")