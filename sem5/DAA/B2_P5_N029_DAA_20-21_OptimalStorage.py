def sortList(list,n):
    sort_length = {}
    for i in range(n):
        sort_length[i] = length[i]
    sort_length = sorted(sort_length.items() , key= lambda x:x[1])
    print("Sorted Lengths: ",sort_length)
    return sort_length

def opticalStorageOnTapes(sortedList,n):
    totalDistance, distance = 0 , 0
    order = [0]*n
    # print(order)
    for i in range(n):
        distance += sortedList[i][1]
        totalDistance += distance
        order[i] = sortedList[i][0]
    mrt = totalDistance/n
    print("Order of arrangement: ",order)
    print("Total distance: ",totalDistance)
    print("Mean retrevial time: ",mrt)

length=list(int(i) for i in input("Enter the lengths of each program:").split())
numberOfPrograms = len(length)

s_List = sortList(length,numberOfPrograms)

opticalStorageOnTapes(s_List,numberOfPrograms)




