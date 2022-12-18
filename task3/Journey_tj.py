#Journey to Jotenheim 
def solve():
    n = int(input())
    keys = list(map(int,input().split()))
    keys.insert(0,n)
    portals = [n]
    j = keys[0]
    for i in range(len(keys)):
        if(j==0):
            break
        j = keys[j]
        portals.append(j)
    if(sorted(portals)[1:]==[1,2,3]):
        print("YES")
    else:
        print("NO")
    
    
    
for _ in range(int(input())):
    solve()