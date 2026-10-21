n = int(input())
nums = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]

new = []
for i in range(n):
    if L - 1 <= i <= R - 1:
        new.append(nums[i] + 1)
    else:
        new.append(nums[i])

print(*new)