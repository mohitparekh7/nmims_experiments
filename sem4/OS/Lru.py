n = 3
l = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1] 
t,pf,f=0,{},0
a=[]
for i in range(n):
    t+=1
    pf[l[i]]=t
    f+=1
    a.append(l[i])
    print("Page",l[i],"added\n",a,"\n")

for i in range(n,len(l)):
    t+=1
    if l[i] not in pf.keys():
        print("Miss")
        p=min(pf.values())
        k=[k for k in pf.keys() if pf[k]==p]
        print("Removing page",k[0])
        pf.pop(k[0])
        pf[l[i]]=t
        f+=1
        a=[l[i] if x==k[0] else x for x in a]
        print("Page",l[i],"added")
    else:
        print("Hit")
        pf[l[i]]=t
    print(a,"\n")
    
print("Page faults:,",f)
print("Page fault ratio:",(f/len(l)))
print("Hit ratio:",((len(l)-f)/len(l)))

