n = int(input())
s = -2
for i in range(n+1):
    if i % 2 == 1:
        s += 3
    else:
        s += 2
print(s)