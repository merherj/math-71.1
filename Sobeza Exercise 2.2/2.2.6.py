n = int(input())
cards = []
for _ in range(n):
    words = input().split()
    value = words[0]
    suit = words[-1]
    cards.append((value, suit))

def color(suit):
    if suit == "Clubs" or suit == "Spades":
        return "black"
    else:
        return "red"

count = 0
for i in range(n):
    scneighbors = 0
    
    if i - 1 >= 0 and color(cards[i - 1][1]) == color(cards[i][1]):
        scneighbors += 1
    
    if i + 1 < n and color(cards[i + 1][1]) == color(cards[i][1]):
        scneighbors += 1
    
    if scneighbors == 1:
        count += 1

print(count)