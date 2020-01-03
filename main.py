fnam = "words-13/words-13-data.txt"

with open(fnam) as f:
    words = [w.strip() for w in f.readlines()]

with open(fnam) as f:
    for line in f.readlines():
        start = line[0:5]
        goal = line[6:11]
        # ... sök väg från start till goal här