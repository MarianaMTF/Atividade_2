sexo=input("digite seu sexo:")
idade = int(input("digite sua idade: "))

if sexo=="masculino" and idade>=21:
    print("você eh maior de idade")
elif sexo=="masculino" and idade<21:
    print("você eh menor de idade")
elif sexo=="feminino" and idade>=18:
    print("você eh maior de idade")
elif sexo=="feminino" and idade<18:
    print("você eh menor de idade")