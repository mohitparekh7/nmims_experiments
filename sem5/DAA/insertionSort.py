def i_sort(arr,n):

    swaps = 0
    comparisons = 0

    for i in range(1,n):

        current_val = arr[i]
        current_pos = i

        comparisons+=1          #comparison  

        while current_pos >0 and  arr[current_pos-1] > current_val:
            arr[current_pos] = arr[current_pos-1]
            current_pos -=1
            comparisons+=1
            swaps+=1
           
        arr[current_pos] = current_val
        print(arr)
        
    print("Swaps : ",swaps)
    print("Comparisons: ",comparisons)
        

n = int(input("Enter number of terms: "))
arr = []

for i in range(n):
    x = int(input("enter the term: "))
    arr.append(x)


i_sort(arr,n)
print("final array: ",arr)
