text = input().strip().lower().split()

def count_word_frequencies(text):
    frequency = {}
    for word in text:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

freq = count_word_frequencies(text)
print(len(freq))
result = []
for key, value in freq.items():
    result.append(f"{key}: {value}")
result.sort()
print(", ".join(result))
