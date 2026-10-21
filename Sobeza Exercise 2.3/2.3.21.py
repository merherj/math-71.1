n, m = [int(x) for x in input().split()]

best = []
winner = []

x = 0
while x < n:
    best.append(0)
    winner.append("UNSOLD")
    x += 1

i = 0
while i < m:
    name, bid, num = input().split()
    bid = int(bid)
    num = int(num) - 1

    if bid > best[num]:
        best[num] = bid
        winner[num] = name

    i += 1

j = 0
while j < n:
    print(winner[j])
    j += 1