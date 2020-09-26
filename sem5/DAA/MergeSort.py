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

        print("mid: ",mid)
        print("Current Sequence: ",array)
        mergeSort(leftArray)
        # print("mid: ",mid)
        # print("Current Sequence(on left): ",array)
        mergeSort(rightArray)
        # print("mid: ",mid)
        # print("Current Sequence (on right): ",array)
        merge(array,leftArray,rightArray)
        print("Current Sequence after merge: ",array)

#array = [-8, 5, 1, 0, -29, 26, 47, 10, 99, 23]
array = [int(i) for i in input("Enter the Array Elements: ").split(',')]
mergeSort(array)
print("Sorted array: ",array)
