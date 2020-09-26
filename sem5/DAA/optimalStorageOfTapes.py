def merge(array,L,R):
    i,j,k = 0,0,0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1
    
    while i <len(L):
        array[k]=L[i]
        i+=1
        k+=1
    while j < len(R):
        array[k]=R[j]
        j+=1
        k+=1

def mergeSort(array):
    n = len(array)
    if n > 1:
        mid = n//2
        leftArray = array[:mid]
        rightArray = array[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)
        merge(array,leftArray,rightArray)

def optimalStorageTime(n,st,ft):
    s, f = [], []
    mergeSort(st)
    mergeSort(ft)
    k = 0
    for i in range(n):
        if i == 0:
            s.append(st[i])
            f.append(ft[k])
            k+=1
            
        elif st[i]>= f[k-1]:
            s.append(st[i])
            f.append(ft[i])
            k+=1
    print('Star times: ',s)
    print('Finish times: ',f)


startTime = [int(i) for i in input("Enter the Start time: ").split(',')]
n1 = len(startTime)
finishTime = [int(i) for i in input("Enter the finsih time: ").split(',')]
n2 = len(finishTime)

if n1 ==n2:
    n = n1
    optimalStorageTime(n,startTime,finishTime)
else:
    print("number of elements of start time and finish time does not match")
