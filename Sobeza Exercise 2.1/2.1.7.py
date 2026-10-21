n = int(input())
nums = [int(x) for x in input().split()]

odd = []
even = []
for x in nums:
    if x % 2 == 1:
        odd.append(x)
    else:
        even.append(x)

odd.sort()
even.sort()

print(*odd)
print(*even)