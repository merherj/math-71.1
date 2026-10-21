n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

face_cards = ("King", "Queen", "Jack")

new = []
for i in range(n):
    if i - 1 >= 0 and cards[i - 1][0] in face_cards:
        new.append(cards[i])

if len(new) == 0:
    print("no cards")
else:
    for value, suit in new:
        print(value, "of", suit)