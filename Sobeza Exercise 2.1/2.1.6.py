n = int(input())

for _ in range(n):
    line = input().split()
    x = int(line[2])
    oe = line[4][:-1]

    even = x % 2 == 0
    state = (oe == 'even')

    if even == state:
        print('CORRECT')
    else:
        print("INCORRECT")
