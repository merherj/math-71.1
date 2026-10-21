n = int(input())
lines = [int(input()) for _ in range(n)]

for i in lines:
    if i % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
