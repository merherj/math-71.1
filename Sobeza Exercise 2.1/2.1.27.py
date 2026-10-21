n = int(input())
moves = input()

opposite = []
for move in moves:
    if move == "N":
        opposite.append("S")
    elif move == "S":
        opposite.append("N")
    elif move == "E":
        opposite.append("W")
    else:
        opposite.append("E")

new = opposite[::-1]

print("".join(new))