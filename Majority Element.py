n = int(input())
lst = [int(x) for x in input().split()]

lst.sort()

def Me(X,n):
    for i in range(len(lst)):
        ce  = X[i]
        count = 0
    
        for j in range(len(lst)):
            if ce == X[j]:
                count +=1
                if count > n/2:
                    return 1
        if count >n/2:
            return 1
        
    return 0
    

print(Me(lst,n))

