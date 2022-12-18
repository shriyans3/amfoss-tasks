#Monster Slayer
def solve():
    n = int(input())
    monsters = list(map(int,input().split()))
    ans = "YES"
    for i in range(len(monsters)-1,0,-1):
        if monsters[i]%min(monsters) != 0:
            ans = "NO"
            break
        
    print(ans)
    
for _ in range(int(input())):
    solve()