
L = [int(x) for x in input().split()]
for x in L:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")