n = int(input())
L = [int(input()) for _ in range(n)]
result_list = []
for x in L:
    result_list.append(str(x % 2))
result_str = "".join(result_list)
print(result_str)