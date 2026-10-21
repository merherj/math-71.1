n = int(input())
nums = [int(x) for x in input().split()]

nums.sort()

count = 1
for i in range(1, n):
    if nums[i] != nums[i - 1]:
        count = count + 1

print(count)