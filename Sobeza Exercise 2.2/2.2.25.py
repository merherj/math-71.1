n, k, x = [int(v) for v in input().split()]

min = 0
max = 0
for _ in range(n):
    chest = [int(v) for v in input().split()]
    
    s = chest[0]
    l = chest[0]
    for value in chest:
        if value < s:
            s = value
        if value > l:
            l = value
    
    min = min + s
    max = max + l

if max < x:
    print("NEVER")
elif min >= x:
    print("ALWAYS")
else:
    print("SOMETIMES")