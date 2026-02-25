def analyze_symmetry(numbers):
    n = len(numbers)
    first_half = numbers[:n//2]
    if n % 2 == 1:
        second_half = numbers[n//2+1:]
    else:
        second_half = numbers[n//2:]
    
    second_half = second_half[::-1]

    if first_half == second_half:
        print("Symmetric")
    elif sum(first_half) == sum(second_half):
        print("Balanced")
    else:
        print("Unordered")

numbers = list(map(int, input().split()))
analyze_symmetry(numbers)
