def getMaxValue(W,wt,pf,n,ratioList):
    totalValue = 0
    orderList = []
    for i in range(n):
        ele = ratioList[i]
        orderList.append(ele[1])
    # print(orderList)

    for i in orderList:
        curwt = wt[i]
        curpf = pf[i]
        if W - curwt >=0:
            W -= curwt
            totalValue += curpf
        else:
            fraction = W/curwt
            totalValue += curpf*fraction
            W = int(W - (curwt*fraction))
            break
    return totalValue
        
def fractionalKnapSack(W,wt,pf,n):
    
    ratioList = []  #pi/wi list 
    for i in range(n):
        r1 = pf[i]
        r2 = wt[i]
        r = r1 / r2 
        ratioList.append([r,i])
    # print(ratioList)

    ratioList.sort(reverse=True)
    # print(ratioList)
    return getMaxValue(W,wt,pf,n,ratioList)


# list of weights  
# weightList = [10, 20, 30]
weightList = [int(i) for i in input("Enter the Weights: ").split(',')]

# no of weights
n1 = len(weightList)

#list of profits corresponding to the weights
# profitList = [60, 140, 120]
profitList = [int(i) for i in input("Enter the Profit values: ").split(',')]

#no of profit units
n2 = len(profitList)

# initialize the weight of the bag 
W = 50

if n1 == n2:
    n = n1
    maxProfit = fractionalKnapSack(W,weightList,profitList,n)
    print("Maximum profit : ",maxProfit)
else:
    print("mismatched no.of values")
