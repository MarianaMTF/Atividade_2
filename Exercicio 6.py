nome=input("digite seu nome:")
media=float(input("digite sua media:"))
faltas=int(input("digite suas faltas:"))

if media>=7 and faltas<=32:
    print(nome +"foi aprovado com media maior que 7 e numero de faltas menor ou igual a 32")
elif media<7 and faltas<=32:
    print(nome +"foi reprovado com media menor que 7, mas numero de faltas menor ou igual a 32")
elif media >= 7 and faltas > 32:
    print(nome +"tem media maior que 7, mas reprovado por numero de faltas maior que 32")
elif media<7 and faltas>32:
    print(nome +"foi reprovado por media menor que 7 e numero de faltas maior que 32")