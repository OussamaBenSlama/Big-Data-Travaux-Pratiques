import sys
 
for line in sys.stdin:
    words = line.strip().split(' ')
    for word in words :
        word = word.lower()
        print(word , "\t" , 1 )
 


    
