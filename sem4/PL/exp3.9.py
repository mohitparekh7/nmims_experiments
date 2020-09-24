x = []
count = 0
while True:
    l = input()
    if l:
        x.append(l.upper())
        count = count + 1
    else:
        break

for i in range(count):
    print(x[i])
