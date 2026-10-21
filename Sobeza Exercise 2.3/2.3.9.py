def average(h, L, R):
    total = 0
    i = L - 1
    while i < R:
        total += h[i]
        i += 1
    return total / (R - L + 1)

def count(h, L, R, k):
    c = 0
    i = L - 1
    while i < R:
        if h[i] <= k:
            c += 1
        i += 1
    return c

def increase(h, L, R, k):
    i = L - 1
    while i < R:
        h[i] += k
        i += 1

def sort_flowers(h, sign):
    if sign == "+":
        h.sort()
    else:
        h.sort(reverse=True)


n = int(input())
h = [int(x) for x in input().split()]
Q = int(input())

q = 0
while q < Q:
    op = input().strip()
    data = input().split()

    if op == "AVERAGE":
        print(f"{average(h, int(data[0]), int(data[1])):.2f}")
    elif op == "COUNT":
        print(count(h, int(data[0]), int(data[1]), int(data[2])))
    elif op == "INCREASE":
        increase(h, int(data[0]), int(data[1]), int(data[2]))
    else:
        sort_flowers(h, data[0])

    q += 1