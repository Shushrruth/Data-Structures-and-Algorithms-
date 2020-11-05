fib = [0,1]

n =int(input())

i = 0
while i <=10**7:
    fib.append(fib[-1]+fib[-2])
    i +=1 
    
def ans(x):
    return fib[x]


print(ans(n)%10)