n = int(input())
nums = [int(x) for x in input().split()]

new = []
for x in nums:
    x += 1
    new.append(x)

print(*new)