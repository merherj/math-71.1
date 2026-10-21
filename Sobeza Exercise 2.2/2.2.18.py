n, x = [int(v) for v in input().split()]

names = []
numbers = []
for _ in range(n):
    parts = input().split()
    names.append(parts[0])
    numbers.append(int(parts[1]))

count = 0
win = None
for i in range(n):
    if numbers[i] == x:
        count += 1
        win = i

if count == 1:
    print(names[win])
else:
    print("no winner")