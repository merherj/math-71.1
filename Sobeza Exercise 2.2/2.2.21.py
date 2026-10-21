def mix(x, y):
    if x == "A" and y == "A":
        return "C"
    elif x == "A" and y == "B":
        return "A"
    elif x == "A" and y == "C":
        return "B"
    elif x == "B" and y == "A":
        return "A"
    elif x == "B" and y == "B":
        return "B"
    elif x == "B" and y == "C":
        return "C"
    elif x == "C" and y == "A":
        return "B"
    elif x == "C" and y == "B":
        return "C"
    else:
        return "A"

n = int(input())
chems = input().split()

result = chems[0]
for i in range(1, n):
    result = mix(result, chems[i])

print(result)