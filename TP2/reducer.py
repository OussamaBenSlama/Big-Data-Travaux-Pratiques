import sys

word = "" 
count = 0
for line in sys.stdin:
    item = line.strip().split('\t')
    if(word == "" or item[0] == word) :
        count += 1
        word = item[0]
    else :
        print(word, "\t" , count)
        word = item[0]
        count = 1

print(word, "\t" , count)
    
