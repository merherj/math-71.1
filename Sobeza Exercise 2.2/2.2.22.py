s = input()

new = []
p = False
for x in s:
    if p:
        new.append(x)
    else:
        if x == ".":
            new.append(x)
            p = True
        else:
            new.append("*")

print("".join(new))