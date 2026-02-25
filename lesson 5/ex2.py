n = int(input())

i = 2
arr = []
while i * i <= n:
    while n % i == 0:
        arr.append(i)
        n //= i
    i += 1

for i in range(len(arr)):
    count = 0
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j] and arr[i] != 0:
            count += 1
            arr[j] = 0
    if count > 0:
        print(f"{arr[i]} {count+1}")

