from collections import Counter

# Open the file in read mode
with open('in', 'r') as file:
    lists = [[], []]
    for line in file:
        values = line.split()
        for idx, value in enumerate(values):
            lists[idx].append(int(value));

    lists[0].sort()
    lists[1].sort()

    diff = []
    for f, b in zip(lists[0], lists[1]):
        diff.append(abs(f-b))

    print("Sum1: " + str(sum(diff)))

    counts = Counter(lists[1])
    sum2 = 0
    for v in lists[0]:
        sum2 += v * counts[v]
        
    print("Sum2: " + str(sum2))

        