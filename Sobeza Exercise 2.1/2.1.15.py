n = int(input())
nums = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]

new = []
for i in range(n):
    if i < L - 1:
        new.append(R)
    else:
        new.append(nums[i])

print(*new)