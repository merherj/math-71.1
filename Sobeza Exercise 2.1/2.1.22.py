n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))
wsuit = input()

new = []
for value, suit in cards:
    if suit == wsuit:
        new.append((value, suit))

if len(new) == 0:
    print("no cards")
else:
    for value, suit in new:
        print(value, "of", suit)