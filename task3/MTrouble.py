#Money Trouble
n , m = map(int,input().split())
ans = -1
two = n//2
one = n%2
if(m>n):
    print(-1)
elif(m==n):
    print(m)
else:
    while(two>0):
        if((two+one)%m==0):
            ans = two+one
            break
        else:
            two -= 1
            one += 2
    print(ans)        
    