def binarySearch(arr,l,r,x):
    # print("low,high,key:",[l,r,x])
    if r >= l: 
        mid = int((l+r)/2)
        # print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1

def findPeak(array):
    i=0
    maxNumber = array[0]
    n = len(array)
    for i in range(1,n):
        if maxNumber < array[i]:
            maxNumber = array[i]
        else:
            break
    
    return [maxNumber,i-1]

def bitonicSearch(subArray,key):
    # print("Subarray:",subArray)
    if len(subArray)>=1:
        l1 = findPeak(subArray)
        # print("L1:",l1)
        peak = l1[0]
        # print("peak:",peak)
        peakAtPosition = l1[1]
        leftArray=subArray[:peakAtPosition]
        rightArray = subArray[peakAtPosition+1:]
        # print("left,right: ",leftArray,rightArray)
        if key == peak:
            print("element found")
        else:
            ans = binarySearch(leftArray,0,len(leftArray)-1,key)
            if ans == -1:
                bitonicSearch(rightArray[::-1],key)
            else:
                print("element found")
    else:
        print("element not found")

# array = [4, 9, 10, 20, 16, 3, 17, 5, 1]
# key = 3
array = [int(i) for i in input("Enter the Array Elements: ").split(',')]
key = int(input("Enter the key: "))
bitonicSearch(array,key)