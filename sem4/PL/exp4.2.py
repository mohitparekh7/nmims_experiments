str = "I am a student";
l = {}

for i in str:
    if i in l:
        l[i] += 1;
    else:
        l[i] = 1;
print(l);

