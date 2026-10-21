n = int(input())
nums = [int(x) for x in input().split()]

new = []
for x in nums:
    if x > 5:
        x -= 5
        new.append(x)
    else:
        new.append(x)

print(*new)