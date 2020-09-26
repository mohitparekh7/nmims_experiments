def maxoftwo(a,b):
    if(a > b):
        return a
    else:
        return b

def minofTwo(a,b):
    if (a<b):
        return a
    else:
        return b

def maxMin(array,i,j):
    if (j - i) <= 1:  
        # print("in if")
        M1 = maxoftwo(array[i],array[j])
        M2 = minofTwo(array[i],array[j])
        l = [i,j ,M1,M2]
        print(l)
        return (M1,M2) 
    else:
        # print("in else")
        mid = int((i + j)/2)
        # print(mid)
        (max1, min1) = maxMin(array,i, mid) 
        l = [i,j ,max1,min1]
        print(l)
        (max2, min2) = maxMin(array,mid+1,j) 
        l = [i,j ,max2,min2]
        print(l)
        
    return (maxoftwo(max1, max2), minofTwo(min1, min2)) 

# number = [-7,6,1,-29,29,4,27,45,16,100,23]
number = [int(i) for i in input("Enter the Array Elements: ").split(',')]
m1,m2 = maxMin(number,0,len(number)-1)
print("Max: ",m1)
print("Min: ",m2)
