n=int(input(""))
l=len(str(bin(n)))-2
for k in range(n+1):
    k=bin(k)
    k=str(k)[2:]
    p=len(k)
    print(" "*(l-p)+k)
    
    
