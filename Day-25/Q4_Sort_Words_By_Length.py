print("Sorting words by length")
import numpy as np
n = int(input("Enter the number of words: "))
words = np.array([input("Enter word {}: ".format(i+1)) for i in range(n)])
for i in range(n):
    for j in range(0, n-i-1):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]
print("Words sorted by length:")
print(words)