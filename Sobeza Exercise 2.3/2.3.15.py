v, t = [int(x) for x in input().split()]

x = 215

i = 0
while i < t:
    x = (512 * x + 227) % 2027
    i += 1

k = 0
while x != v:
    x = (512 * x + 227) % 2027
    k += 1

print(k)