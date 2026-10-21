n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

face_cards = ("Jack", "Queen", "King")

count = 0
for value, suit in cards:
    if value in face_cards:
        count += 1

print(count)