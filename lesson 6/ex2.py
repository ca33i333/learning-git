n = int(input())
numbers = list(map(int, input().split()))

def find_median(numbers):
    numbers.sort()
    if n % 2 == 0:
        return (numbers[n//2-1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]
    
x = find_median(numbers)
print(f"{x:.1f}")