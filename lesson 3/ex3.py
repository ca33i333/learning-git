import math

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def is_friendly(n):
    rev = reverse_number(n)
    return math.gcd(n, rev) == 1


n = int(input())
if is_friendly(n):
    print("Friendly number")
else:
    print("Not a friendly number")
