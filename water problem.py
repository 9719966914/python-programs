r=5
h=10
Vwtr=15
t=eval(input('enter the time'))
Vc=3.14*r**2*h
Vwtr= 15*t
if Vwtr > Vc:
    print('overflow')

elif Vwtr==Vc:
    print('tank is full')

else:
    print('underflow')
    
