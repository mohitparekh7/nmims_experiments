def binarySearch(array,i,j,element):
	if j >=i:
		mid = int((i+j)/2)

		if array[mid]==element:
			return mid
		
		elif array[mid]>x:
			return binarySearch(array,i,mid-1,element)

		else:
			return binarySearch(array,mid+1,j,element)

	else:
		return -1



arr = input("Enter the string elements: ").split(",")
print(arr)

x = input("Enter string to be searched for:")
answer = binarySearch(arr,0,len(arr)-1,x) 

if answer==-1:
	print("element not found")
else:
	print("Element found at: ",answer+1)