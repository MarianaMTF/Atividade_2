z=int(input("digite o valor de z:"))
w=int(input("digite o valor de w:"))

if w>0 or z<7:
    x=(5*w+1)/3
    t=5*z+2
    y=(7*(x*3))-(3*(x*0.5))-(8*t)/5*(x+1)
    print("o calculo resultado:"+str(y))
else:
    x=5*z+2
    t=(5*w+1)/3
    y=(7*(x*3))-(3*(x*0.5))-(8*t)/5*(x+1)
    print("o calculo resultado:"+str(y))