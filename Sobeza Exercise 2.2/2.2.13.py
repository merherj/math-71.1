n = int(input())
prices = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

total = 0
for i in range(n):
    total = total + prices[i] * q[i]

print(total)