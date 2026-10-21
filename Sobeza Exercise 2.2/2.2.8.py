n = int(input())
nums = [int(x) for x in input().split()]

d = nums[1] - nums[0]

is_arithmetic = True
for i in range(1, n):
    if nums[i] - nums[i - 1] != d:
        is_arithmetic = False

if is_arithmetic:
    print("YES")
    print("initial term:", nums[0])
    print("common difference:", d)
else:
    print("NO")