n = int(input())
temps = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]

reac = -1
for i in range(L - 1, R):
    if temps[i] > 50 and reac == -1:
        reac = i + 1

if reac == -1:
    print("no reaction")
else:
    print(reac)