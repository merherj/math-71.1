n = int(input())
nums = [int(x) for x in input().split()]

min = nums[0]
for i in range(1, n):
    if nums[i] < min:
        min = nums[i]

print(min)