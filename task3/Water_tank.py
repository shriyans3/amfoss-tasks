#Water Tank Blues
def solve():
    n = int(input())
    tanks = list(map(int,input().split()))
    shifted = 0
    if(tanks[:-1].count(0)==len(tanks)-1):
        print(0)
    elif(0 not in tanks):
        print(sum(tanks[:-1]))
    else:
        for i in range(n):
            for j in range(i+1,n):
                if (tanks[i]>1 and tanks[j]==0) and (0 not in tanks[i+1:j]):
                    shifted += 1
                    tanks[i] -= 1
                    tanks[j] += 1
        #print(tanks)
        print(sum(tanks[:-1])+shifted)
for _ in range(int(input())):
    solve()