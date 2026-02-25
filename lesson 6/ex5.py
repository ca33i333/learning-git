numbers = list(map(int, input().split()))

x = abs(max(numbers))
for i in range(1, x+2):
    if i not in numbers:
        print(i)
        break

i = 1
while i in numbers:
    i += 1
print(i)
