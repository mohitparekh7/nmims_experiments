x = input("enter the string")
d = 0
l = 0
for i in x:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
print("letters :",l)
print("digits :",d)

