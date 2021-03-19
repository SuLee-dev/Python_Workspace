from collections import deque
import copy

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

n = int(input())

s = []

for _ in range(n):
    s.append(list(map(int, input().split())))


count = 0
def bfs(a, b):
    global count
    count -= 1
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

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            bfs(i, j)

ans = 10000
def bfs2(z):
    global ans
    queue = deque()
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == z:
                dist[i][j] = 0
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
                continue
            if s[x1][y1] < 0 and s[x1][y1] != z:
                ans = min(ans, dist[x][y])
                return
            if s[x1][y1] == 0 and dist[x1][y1] == -1:
                dist[x1][y1] = dist[x][y] + 1
                queue.append([x1, y1])

for i in range(count, 0):
    bfs2(i)

print(ans)