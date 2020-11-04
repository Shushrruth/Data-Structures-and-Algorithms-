# Selection Sort

X = [int(x) for x in input().split()]

def SS(A):
    for i in range(len(A)):
        min = i
        for j in range(i+1,len(A)):
            
            if A[j] < A[min]:
                min = j
            
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
    
    return A
        

print(SS(X))



        

         
                