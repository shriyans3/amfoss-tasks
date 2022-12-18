#Shrink to Win.
n = list(map(int,input()))

count = 0  
while((sum(n)>=10 and len(n)>1)or(sum(n)<10 and len(n)>1)):
    n = [int(x) for x in str(sum(n))]
    count += 1
    
    
print(count)