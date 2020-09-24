def knapSack(W,w1,p1,n):
    if n == 0 or W ==0:
        return 0

    if (w1[n-1]>W):
        return knapSack(W,w1,p1,n-1)

    else:
        return max(p1[n-1]+knapSack(W-w1[n-1],w1,p1,n-1),knapSack(W,w1,p1,n-1))

# list of weights  
weightList = [10, 20, 30]

# no of elements
n = len(weightList)

#list of profits corresponding to the weights
profitList = [60, 100, 120]

# initialize the weight of the bag 
W = 50

print(knapSack(W,weightList,profitList,n))



