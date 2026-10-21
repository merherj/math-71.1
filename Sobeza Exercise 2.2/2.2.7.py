n = int(input())
words = input().split()

first = words[0][0]

all_same = True
for word in words:
    if word[0] != first:
        all_same = False

if all_same == True:
    print(first)
else:
    print("Invalid")