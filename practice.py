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
 
# 이코테 2강 구현

# n = int(input())

# x, y = 1, 1
# plans = input().split()
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# move = ["U", "D", "L", "R"]

# for plan in plans:
#     for i in range(len(move)):
#         if plan == move[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny

# print(x, y)

# h = int(input())
# cnt = 0

# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if "3" in str(i) + str(j) + str(k):
#                 cnt += 1

# print(cnt)

# point = input()
# x, y = 1, 1
# cnt = 8

# rows = ["a", "b", "c", "d", "e", "f", "g", "h"]

# ord 함수 -- int(ord(x))

# for i in range(8):
#     if (rows[i] == point[0]):
#         x = i + 1
#         y = int(point[1])
#         break

# dx = [1, 1, 2, 2, -1, -1, -2, -2]
# dy = [2, -2, 1, -1, 2, -2, 1, -1]

# for i in range(8):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if (nx < 1 or ny < 1 or nx > 8 or ny > 8):
#         cnt -= 1

# print(cnt)

s = list(input())
s.sort()

a = ""
num = 0
for i in s:
    if (i.isnumeric() == True):
        num += int(i)
    else:
        a += i
if (num != 0):
    print(a + str(num))
else:
    print(a)