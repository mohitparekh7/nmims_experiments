def maxi(s):
    n1=0
    n2=0
    for i in range(len(s)):
        if s[i]>="0" and s[i]<="9":
            n1 = n1*10+int(int(s[i])-0)
        else:
            n2=max(n1,n2)
            n1=0
    return max(n1,n2)

s='32ws4ed5rf6gt7'
print(maxi(s))