
n =int(input())

def max(a):
    n = 0
    i =0
    while i <=10000:
        if a >=10:
            a = a-10
            n +=1
        elif a>=5:
            a = a-5
            n +=1
        elif a>=1:
            a = a-1
            n +=1
        i +=1
        
    return n


print(max(n))
        