import sys


zeyed = ['.', ',', '!', '?', ')', '(']

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        word = word.lower()
        for p in zeyed:
            word = word.replace(p, '')
        print(word, "\t", 1)
