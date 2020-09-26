def partition(arr,p,r):
    x = arr[r]
    i = p -1
    for j in range(p,r):
        if arr[j] <= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    print(arr)
    return i + 1
    
def quickSort(arr,p,r):
    if p < r :
        q = partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)
    return arr
        
def numberQuickSort():
    n = int(input("enter no of elements: "))
    A = []
    for i in range(n):
        x = int(input("enter element: "))
        A.append(x)
    #print(A)
    res = quickSort(A,0,n-1)
    print(res)

def stringQuickSort():
    n = int(input("enter no of words: "))
    A = []
    for i in range(n):
        x = input("enter element: ")
        A.append(x)
    # print(A)
    res = quickSort(A,0,n-1)
    print(res)
    
choice = int(input("Enter \n1.For numbers \n2.For strings\n"))
if choice == 1:
    numberQuickSort()
elif choice == 2:
    stringQuickSort()
else:
    print("invalid selection")
