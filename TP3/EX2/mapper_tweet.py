
import sys

bad_words = ["nul" , "insatisfait" , "bof" ,"incompétents"]
good_words = ["super" , "satisfait" , "excellent","merci"]
for line in sys.stdin:
    bad = 0
    good = 0
    words = line.strip().split(" ")
    for word in words :
        if word in bad_words:
            bad += 1
        if word in good_words:
            good += 1 
    if bad == good :
        print(f"{"inconcluant"}\t{1}") 
    elif bad > good :
        print(f"{"insatisfait"}\t{1}")
    else :
        print(f"{"satisfait"}\t{1}")
