lst = [int(x) for x in input().split()]
num = [int(x) for x in input().split()]
lst = lst[1:]
num = num[1:]

def BS(A,low,high,key):
    if high < low:
        return -1
    
    mid = low + round((high-low)/2)
    
    if key == A[mid]:
        return mid
    
    elif key < A[mid]:
        return BS(A,low,mid-1,key)
    
    else:
        return BS(A,mid+1,high,key)
    
    
for i in num:
    print (BS(lst,0,len(lst)-1,i),end =" ")
    
   

