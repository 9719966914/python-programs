a=eval(input('enter the number'))

ini=0

l=[1,2,3,4,5]

point=4
cnt=0

while(True):
    ini+=l[point]
    cnt+=1

    if ini==a:
        print(cnt)
        break
    elif ini<a:
        continue
    elif ini>a:
        ini-=l[point]
        cnt-=1
        point-=1
