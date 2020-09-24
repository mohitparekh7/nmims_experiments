d = {1: 10, 2: 10, 3: 30, 4: 40, 5: 50, 6: 60}
d1 ={}
for k ,v in d.items():
    if v not in d1.values():
        d1[k] = v
print(d1)