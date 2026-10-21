n = int(input())
scores = [int(x) for x in input().split()]

average = sum(scores) / n

below = 0
above = 0
for score in scores:
    if score < average:
        below += 1
    elif score > average:
        above += 1

print(below, "scored below average")
print(above, "scored above average")