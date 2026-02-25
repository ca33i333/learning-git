# Inputs
n = int(input())
numbers = list(map(int, input().split()))

print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(*numbers[::-1])