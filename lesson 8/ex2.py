# Input
numbers = list(map(int, input().split()))

# Define function
def rotate_and_inspect(numbers):
    
    # The rotated list (space-separated).
    numbers = numbers[1:] + numbers[:1]
    print(*numbers)

    # The new minimum value.
    print(min(numbers))
    
    # How many times the original last element appears in the rotated list.
    original_last = numbers[-1]
    print(numbers.count(original_last))

rotate_and_inspect(numbers)