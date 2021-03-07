# 2021/03/05

# 백준 2839.

# def getNum(x):
#     n = x // 5
#     while n >= 1:
#         num = x - 5 * n
#         if num % 3 == 0:
#             return num // 3 + n
#         n -= 1
#     return False


# n = int(input())

# if (n % 5 == 0):
#     print(n // 5)
# elif (getNum(n) != False):
#     print(getNum(n))
# elif (n % 3 == 0):
#     print(n // 3)
# else:
#     print(-1)


# 백준 2775.

# t = int(input())

# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     ap = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
#     for i in range(n + 1):
#         ap[0][i] = i
#     if k > 0:
#         for i in range(1, k + 1):
#             for j in range(1, n + 1):
#                 ap[i][j] = ap[i - 1][j] + ap[i][j - 1]
#     print(ap[k][n])


# 2021/03/06

# 백준 11047.

# n, k = map(int, input().split())

# coin = []

# for _ in range(n):
#     num = int(input())
#     coin.append(num)
# coin.reverse()

# cnt = 0
# temp = k

# for i in range(len(coin)):
#     if (temp >= coin[i]):
#         cnt += temp // coin[i]
#         temp %= coin[i]

# print(cnt)


# 백준 1931. (복습)

# n = int(input())

# timeTable = []

# for i in range(n):
#     con = tuple(map(int, input().split()))
#     timeTable.append(con)

# timeTable = sorted(timeTable, key = lambda x : x[0])
# timeTable = sorted(timeTable, key = lambda x : x[1])

# last, cnt = 0, 0

# for i, j in timeTable:
#     if i >= last:
#         cnt += 1
#         last = j

# print(cnt)


# 백준 11399.

# n = int(input())

# p = list(map(int, input().split()))

# p.sort()

# ans = 0
# temp = 0

# for i in p:
#     temp += i
#     ans += temp

# print(ans)