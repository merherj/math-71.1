move = list(input())

i = 0
x, y = 0, 0
while i < len(move):
    if move[i] == "U":
        y += 1
    elif move[i] == "D":
        y -= 1
    elif move[i] == "R":
        x += 1
    elif move[i] == "L":
        x -= 1

    i +=1
    print(x, y)

