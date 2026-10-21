word = input()
n = int(input())

for _ in range(n):
    pos, l = input().split()
    pos = int(pos) - 1
    word = word[:pos] + l + word[pos + 1:]

print(word)