bag = [int(x) for x in input().split()]

items = []
for i in range(bag[0]):
    items.append([int(x) for x in input().split()])
    

rep = 0
value = []
for j in range(len(items)):
    value.append(items[j][0]/items[j][1])
    rep = rep + items[j][0]
    
imp = [i[0] for i in sorted(enumerate(value), key=lambda x:x[1])]

imp.reverse()


ans = 0
W = bag[1]
while rep !=0:
    
    for i in imp:
        if items[i][1] <= W:
            ans = ans + items[i][0]
            W = W - items[i][1]
            rep = rep - items[i][0]
            
            
        else:
            ans = ans + (W/items[i][1])*items[i][0]
            W = 0
            rep = 0
            
print(ans)
            
            
    
    
    