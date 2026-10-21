s, t = [int(x) for x in input().split()]

i = 0
while s < t:
    if (s == 1 or s == -2) and t > 1:
        print("MOVE ON")
        break
    s = s**2 - 3
    i += 1
else:
    print(i)