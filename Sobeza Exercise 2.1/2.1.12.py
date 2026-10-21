n = int(input())
nums = [int(x) for x in input().split()]

mx = max(nums)

new = []

for i in range(n):
    if nums[i] == mx:
        new.append(i + 1)

print(*new)
