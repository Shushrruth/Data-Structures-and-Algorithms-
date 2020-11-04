d = int(input())
m = int(input())
n = int(input())
l = [int(x) for x in input().split()]
l.append(d)
l.insert(0,0)



def car():
    numR = 0
    currentR = 0 
    while currentR <=n:
        lastR = currentR
        while currentR <= n and l[currentR +1] - l[lastR] <= m:
            currentR = currentR + 1
        if currentR == lastR:
            return -1
        
        if currentR <=n:
            numR = numR + 1
            
    return numR
        
print(car())


 