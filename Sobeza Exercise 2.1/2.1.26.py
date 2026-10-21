n = int(input())
prices = [int(x) for x in input().split()]

new = []
for i in range(1, n):
    diff = prices[i] - prices[i - 1]
    if diff > 0:
        new.append("+" + str(diff))
    elif diff < 0:
        new.append(str(diff))
    else:
        new.append("0")

print(*new)