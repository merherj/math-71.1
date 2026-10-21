n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))
L, R = [int(x) for x in input().split()]

new = []

for i in range(L - 1, R):
    new.append(cards[i])

for i in range(0, L - 1):
    new.append(cards[i])

for i in range(R, n):
    new.append(cards[i])

for value, suit in new:
    print(value, "of", suit)