import random

# list = [2,4,10,12,3,20,30,11,25]
list = [int(i) for i in input("Enter list: ").split(",")]
n  = len(list)
# k = 2
k = int(input("Enter value of k: "))
m1 = random.choice(list)
m2 = random.choice(list)
print("M1 and M2: ",m1,m2)

condition = True
while (condition):
    new_m1 , new_m2 = 0 , 0
    l1, l2 = [] , []
    n1,n2,list1_total,list2_total = 0, 0 , 0 , 0
    for i in range(n):
        x = list[i]
        # print("x : ",x)
        if (abs(x-m2)< abs(x-m1)):
            l2.append(x)
            list2_total += x
            n2+=1
        else:
            l1.append(x)
            list1_total +=x
            n1+=1
    print("Cluster 1",l1)
    print("Cluster 2",l2)
    # print("List1 total and list2 total: ",list1_total,list2_total)
    # print("n1 and n2:",n1,n2)

    new_m1 = list1_total/n1
    new_m2 = list2_total/n2
    print("new_mean1 and new_mean2: ",new_m1,new_m2)
    if(m1==new_m1 and m2 == new_m2):
        condition = False
    else:
        m1 = new_m1 
        m2 = new_m2




