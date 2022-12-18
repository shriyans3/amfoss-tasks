#Hero to Zero
def solve():
    n = int(input())
    hero_levels = list(map(int,input().split()))
    mana = 0
    steps = 0
    hero_levels = sorted(hero_levels)
    
    if(0 not in hero_levels):
        if(len(set(hero_levels))==len(hero_levels)):
            mana += n+1
            print(mana)
            return
    if(0 not in hero_levels):
        if(len(set(hero_levels))!=len(hero_levels)):
            mana += n
            print(mana)
            return
    if(0 in hero_levels):
        mana += n-hero_levels.count(0)
        print(mana)
        
    
    
for _ in range(int(input())):
    solve()