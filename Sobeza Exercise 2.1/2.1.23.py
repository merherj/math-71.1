n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

suit_order = ("Clubs", "Diamonds", "Hearts", "Spades")

new = []
for x in suit_order:
    for value, suit in cards:
        if suit == x:
            new.append((value, suit))

for value, suit in new:
    print(value, "of", suit)