n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

tvalue, tsuit = cards[0]

new = []
for value, suit in cards:
    if value != tvalue and suit != tsuit:
        new.append((value, suit))

if len(new) == 0:
    print("empty deck")
else:
    for value, suit in new:
        print(value, "of", suit)