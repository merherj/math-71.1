n = int(input())
nums = [int(x) for x in input().split()]
add = [int(x) for x in input().split()]

new = []
for i in range(n):
    new.append(nums[i] + add[i])

print(*new)