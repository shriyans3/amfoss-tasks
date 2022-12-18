#DeadShot not completed 
n = int(input())
co_ordinates = []
van_coord = []
vantage_pts = 0
check = 0
r_neighbours = 0
l_neighbours = 0
d_neighbours = 0
u_neighbours = 0
for i in range(n):
    cdinates = list(map(int,input().split()))
    co_ordinates.append(cdinates)
indexs = 0
print(co_ordinates)
for i in range(n):
    for j in range(n):
        if(i!=j):
            x =co_ordinates[i] 
            y = co_ordinates[j]
            if (((x[0]==y[0]) and (abs(x[1]-y[1])>0))):
                d_neighbours += 1
            if (((x[0]==y[0]) and (abs(x[1]-y[1])<0))):
                u_neighbours += 1
            if ((x[1]==y[1]) and (abs(x[0]-y[0])>0)):
                l_neighbours += 1
            if ((x[1]==y[1]) and (abs(x[0]-y[0])>0)):
                r_neighbours += 1
    if (d_neighbours>=1 and u_neighbours>=1 and l_neighbours>=1 and r_neighbours>=1):
        vantage_pts += 1
    r_neighbours = 0
    l_neighbours = 0
    d_neighbours = 0
    u_neighbours = 0
    

print(vantage_pts)
    
