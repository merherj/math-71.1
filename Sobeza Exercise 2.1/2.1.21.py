n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

suit_order = ("Clubs", "Diamonds", "Hearts", "Spades")

bsuit = cards[-1][1]
bstrength = suit_order.index(bsuit)

new = []
for value, suit in cards:
    if suit_order.index(suit) <= bstrength:
        new.append((value, suit))

if len(new) == 0:
    print("empty deck")
else:
    for value, suit in new:
        print(value, "of", suit)