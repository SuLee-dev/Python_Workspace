from collections import deque
import copy

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

n = int(input())

s = []

for _ in range(n):
    s.append(list(map(int, input().split())))


count = -1
def bfs(a, b):
    global count
    queue = deque([[a, b]])
    s[a][b] = count

    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < n and 0 <= y1 < n:
                if s[x1][y1] == 1:
                    queue.append([x1, y1])
                    s[x1][y1] = count
    count -= 1

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            bfs(i, j)
