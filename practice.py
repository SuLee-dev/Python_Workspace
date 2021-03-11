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




# s = list(input())
# s.sort()

# a = ""
# num = 0
# for i in s:
#     if (i.isnumeric() == True):
#         num += int(i)
#     else:
#         a += i
# if (num != 0):
#     print(a + str(num))
# else:
#     print(a)



# 이코테 3강 DFS & BFS

# def gd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gd(b, a % b)

# print(gd(162, 192))




# from collections import deque

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = " ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

       

# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# visited = [False] * 9
# dfs(graph, 1, visited)
# print()
# visited = [False] * 9
# bfs(graph, 1, visited)





# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False

#     if graph[x][y] == 0:
#         graph[x][y] == 1

#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True
#     else:
#         return False


# n, m = map(int, input().split())

# ice = []
# for i in range(n):
#     ice.append(list(map(int, input())))

# cnt = 0

# bfs

# visited = []
# for i in range(n * m):
#     x, y = i // m, i % m
#     if (ice[x][y] == 0 and i not in visited):
#         visited.append(i)
#         queue = deque([i])
#         while queue:
#             v = queue.popleft()
#             if (v % m < m - 1):
#                 if ice[v // m][v % m + 1] == 0 and v + 1 not in visited:
#                     queue.append(v + 1)
#                     visited.append(v + 1)
#             if (v % m > 0):
#                 if ice[v // m][v % m - 1] == 0 and v - 1 not in visited:
#                     queue.append(v - 1)
#                     visited.append(v - 1)
#             if (v // m < n - 1):
#                 if ice[v // m + 1][v % m] == 0 and v + m not in visited:
#                     queue.append(v + m)
#                     visited.append(v + m)
#         cnt += 1


# dfs

# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             cnt += 1


# print(cnt)