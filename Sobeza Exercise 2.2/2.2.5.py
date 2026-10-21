n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

first_value = cards[0][0]

count = 0
for value, suit in cards:
    if value == first_value:
        count += 1

print(count)