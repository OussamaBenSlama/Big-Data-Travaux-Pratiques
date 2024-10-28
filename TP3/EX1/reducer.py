import sys
from collections import defaultdict

anagrams = defaultdict(list)

for line in sys.stdin:
    sorted_word, word = line.strip().split("\t")
    anagrams[sorted_word].append(word)

for sorted_word, words in anagrams.items():
    if len(words) > 1: 
        print(f"{', '.join(words)}")
