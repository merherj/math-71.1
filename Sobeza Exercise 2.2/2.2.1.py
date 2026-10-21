n, p = input().split()
n = int(n)
words = input().split()

count = 0
for word in words:
    if word[0] == p:
        count += 1

print(count)