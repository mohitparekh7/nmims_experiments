def mst(v,dis):
    d = [1000] * len(v)
    d[0] = 0
    # print("d: ",d)
    parent = [0] * len(v)
    # print("parent array: ",parent)
    visited = [0] * len(v)
    # print(visited)
    strt = 0
    while 0 in visited:                 # run the loop till all the vertices are visited
        index = strt
        visited[index] = 1
        ans = {}
        a = []
        visited[index]=1
        for j in range(len(v)):
            if dis[index][j]!=-1:
                a.append(j)
        for ele in a:
            if visited[ele]!=1:
                if d[ele] ==1000 or d[ele] > dis[index][j]:
                    d[ele]= dis[index][ele]
                    parent[ele]=index
        min = 1000
        for x in range(len(v)):
            if d[x]<min and visited[x]!=1:
                min = d[x]
                pos = x
        strt = pos
    # print(d)
    mincost = 0
    for i in range(len(d)):
        mincost += d[i]
    for i in range(len(v)):
        ans[v[i]] = d[i]
    print(ans)
    print("Minimum Cost : ",mincost)

v = [str(i) for i in input("Enter the vertices: ").split(',')]
#v = ['a', 'b', 'c', 'd']
# print(v)
# print(len(v))
dis = []
# dis = [[0, 20, 10, 60],[20, 0, 30, 80],[10, 30, 0, 10],[60, 10, 10, 0]]
for i in range(len(v)):
    x = [int(i) for i in input("Enter the distance from {} to other vertices : ".format(v[i])).split(',')]
    dis.append(x)
print(dis)
mst(v,dis)