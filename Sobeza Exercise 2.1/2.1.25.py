n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

top_pile = []
for i in range(0, n // 2):
    top_pile.append(cards[i])

bottom_pile = []
for i in range(n // 2, n):
    bottom_pile.append(cards[i])

new = []
for i in range(n // 2):
    new.append(top_pile[i])
    new.append(bottom_pile[i])

for value, suit in new:
    print(value, "of", suit)