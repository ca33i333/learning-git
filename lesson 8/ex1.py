# Inputs
n = int(input())
scores = list(map(int, input().split()))
k = int(input())

# Define function
def score_report(scores, k):
    
    # Print the average score to two decimals.
    avg = sum(scores) / len(scores)
    print(f"{avg:.2f}")

    # Print the range of scores (max - min).
    print(max(scores)-min(scores))

    # Print the number of distinct scores.
    print(len(set(scores)))

    # Print the top–k scores in descending order (if k exceeds the list length, print all).
    # 100 90 80 80 70
    top_k = sorted(scores, reverse=True)[:k]
    print(*top_k)

score_report(scores, k)