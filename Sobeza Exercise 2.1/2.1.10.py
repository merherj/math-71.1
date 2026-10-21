n = int(input())
nums = [int(x) for x in input().split()]

mn = min(nums)
mx = max(nums)

result = []
for x in nums:
    if x == mn:
        result.append(mx)
    else:
        result.append(x)

print(*result)