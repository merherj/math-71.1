s = input()

a_index = s.index("a")
b_index = s.index("b")

low = min(a_index, b_index)
high = max(a_index, b_index)

new = []
for i in range(len(s)):
    if low < i < high:
        new.append("*")
    else:
        new.append(s[i])

print("".join(new))