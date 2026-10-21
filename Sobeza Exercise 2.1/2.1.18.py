n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

new = cards.copy()
new[0], new[-1] = new[-1], new[0]

for value, suit in new:
    print(value, "of", suit)

# new = []
# for i in range(n):
#     if i == 0:
#         new.append(cards[-1])
#     elif i == n - 1:
#         new.append(cards[0])
#     else:
#         new.append(cards[i])