# def stick(AnyList, l, d, x, y):
#     if (d == 0):
#         for i in range(l):
#             if AnyList[x - 1][i + y - 1] == 0:
#                 AnyList[x - 1][i + y - 1] = 1
#     elif (d == 1):
#         for i in range(l):
#             if AnyList[i + x - 1][y - 1] == 0:
#                 AnyList[i + x - 1][y - 1] = 1        

# h, w = map(int, input().split())

# board = [[0 for i in range(w)] for j in range(h)]

# n = int(input())

# for i in range(n):
#     l, d, x, y = map(int, input().split())
#     stick(board, l, d, x, y)

# for i in range(h):
#     for j in range(w):
#         print(board[i][j], end = " ")
#     print()

# from itertools import *

# data = ["a", "b", "c"]

# result = list(permutations(data, 3))
# print(result)
# result2 = list(combinations(data, 2))
# print(result2)
# result3 = list(product(data, repeat = 2))
# print(result3)
# print(sorted(result3, key = lambda x : x[0], reverse = True))
# result4 = list(combinations_with_replacement(data, 2))
# print(result4)

# from collections import *

# counter = Counter([1, 2, 3, 3, 2, 2])

# print(counter[1])
# print(counter[2])
# print(counter[3])
# print(dict(counter))

# import math

# print(math.gcd(18, 27))
# print((lambda a, b : a * b // math.gcd(a, b))(18, 27))