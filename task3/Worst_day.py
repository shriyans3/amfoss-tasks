# The Worst day to miss school
n = int(input())
group_list = list(map(int,input().split()))
new_list = sorted(group_list)

count_four = new_list.count(4)
count_three = new_list.count(3)
count_two = new_list.count(2)
count_one = new_list.count(1)
grps = 0
grps += count_four
three = []
two = []
one = []
for i in range(len(group_list)):
    if(group_list[i]==1):
        one.append(1)
    elif(group_list[i]==2):
        two.append(2)
    elif(group_list[i]==3):
        three.append(3)

total = [one,two,three]
for i in range(len(three)):
    if(len(one)!=0):
        one.remove(1)
        three[i] += 1
grps += len(three)
one_two = (sum(one)+sum(two))
if((one_two)%4==0):
    grps += one_two//4
else:
    grps += (one_two//4)+1
    
print(grps)



    
    

