
import sys

for line in sys.stdin:
    word = line.strip()
    sorted_word = ''.join(sorted(word))  
    print(f"{sorted_word}\t{word}")     
