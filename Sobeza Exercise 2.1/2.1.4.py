L, R = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
for i in range(L, R+1):
    nums[i] *= -1
print(*nums)