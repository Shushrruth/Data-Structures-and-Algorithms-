x, y = [int(x) for x in input().split()]

def gcd(a,b):
    if a < b:
        m = a
        n = b
    elif a > b:
        m = b
        n = a
    else:
        return a
    
    i = 0
    while i <=10000:
        temp = m
        m = n%m
        n = temp
        i +=1
        if m ==0:
            return n
    

        
           
print(int((x*y)/gcd(x,y)))