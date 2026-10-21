def faro(s):
    top = s[:int(n/2)]
    bottom = s[int(n/2):]

    shuffle = []
    for i in range(int(n/2)):
        shuffle.append(top[i])
        shuffle.append(bottom[i])
    return shuffle

n = int(input())
orig = list(range(n))

shuffle = faro(orig)
counter = 1
while shuffle != orig:
    shuffle = faro(shuffle)
    counter += 1

print(counter)





# n = int(input())

# original = []
# i = 0
# while i < n:
#     original.append(i)
#     i += 1

# deck = original
# k = 0

# while True:
#     half = n // 2
#     new = []
#     j = 0
#     while j < half:
#         new.append(deck[j])        
#         new.append(deck[half + j])  
#         j += 1
#     deck = new
#     k += 1

#     if deck == original:
#         break

# print(k)