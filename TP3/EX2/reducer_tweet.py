import sys
from collections import defaultdict

occ = defaultdict(int)  

for line in sys.stdin:
    tweet, _ = line.strip().split("\t") 
    occ[tweet] += 1  

for tweet, count in occ.items():
    print(f"{tweet}\t{count}")