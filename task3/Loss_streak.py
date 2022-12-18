#Losing Streak
x , y = map(int,input().split())
p = y//x
a = 0
if x==y:
    print(0)
elif x%y != 0:
    print(-1)
else:
    while(p!=1):
        if p%3 == 0:
            a += 1
            p = p/3
        if p%2 == 0:
            a += 1
            p = p/2
        else:
            print(-1)
            exit()
        
    print(a)
        