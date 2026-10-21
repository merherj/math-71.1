n = int(input())
nums = [int(x) for x in input().split()]

new = []

for i in range(n):
    tleft = i - 1 < 0 or nums[i] > nums[i - 1]
    tright = i + 1 >= n or nums[i] > nums[i + 1]
    if tleft and tright:
         new.append(i + 1)

if len(new) == 0:
    print("none")
else:
    print(*new)