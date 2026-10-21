n = int(input())
nums = [int(x) for x in input().split()]

min = None
for i in range(n):
    if nums[i] != 0:
        if min == None or nums[i] < min:
            min = nums[i]

print(min)