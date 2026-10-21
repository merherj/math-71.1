L = int(input())
nums = [int(x) for x in input().split()]
for i in range(L, len(nums)):
    nums[i] *= -1
print(*nums)