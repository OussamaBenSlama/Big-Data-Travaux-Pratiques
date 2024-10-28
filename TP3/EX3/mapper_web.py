import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    pi, references = line.split(" : ")
    pi = pi.strip()
    references = references.split(", ")
    for pj in references:
        print(f"{pj.strip()}\t{pi}")
