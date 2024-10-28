import sys
from collections import defaultdict

pj_references = defaultdict(list)
for line in sys.stdin:
    pj , pi = line.split('\t')
    pj_references[pj].append(pi)

for pj, pis in pj_references.items():
        print(f"{pj}:{', '.join(pis)}")
