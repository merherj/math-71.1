n = int(input())
nums = [int(x) for x in input().split()]

leven = -1
for i in range(n):
    if nums[i] % 2 == 0:
        leven = i

if leven == -1:
    print("no even numbers")
else:
    print(leven)