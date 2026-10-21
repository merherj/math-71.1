n = int(input())
nums = [int(x) for x in input().split()]

c = True
nd = True
ni = True

for i in range(1, n):
    if nums[i] != nums[i - 1]:
        c = False
    if nums[i] < nums[i - 1]:
        nd = False
    if nums[i] > nums[i - 1]:
        ni = False

if c:
    print("constant")
elif nd:
    print("nondecreasing")
elif ni:
    print("nonincreasing")
else:
    print("not sorted")