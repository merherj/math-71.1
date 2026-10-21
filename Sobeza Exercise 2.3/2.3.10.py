p, x = [int(x) for x in input().split()]

days = 0
while p < x:
    p += (p // 100)
    days += 1

print(days)