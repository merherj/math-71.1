n = int(input())
words = input().split()

result = words[0]
for i in range(1, n):
    result = result + "::" + words[i]

print(result)