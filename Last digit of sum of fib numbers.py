a = 0
b = 1

n = int(input())


sum = 0
i=0 
while i <=(n-2):
    c = (((a + b)%10)**2)%10
    a = b%10
    b = c%10
    sum = (sum + c)%10
    i +=1
    

def fab(a):
    if a==0:
        return 0
    else:
        return sum%10

print(fab(n))
    






    