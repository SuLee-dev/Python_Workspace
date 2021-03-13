from collections import deque
import sys

count = []
n = int(sys.stdin.readline())

s = []
for _ in range(n):
    s.append(list(sys.stdin.readline()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    dq = deque([[a, b]])
    cnt = 1
    s[a][b] = "0"
    while dq:
        v = dq.popleft()
        x, y = v[0], v[1]

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < n and 0 <= y1 < n and s[x1][y1] == "1":
                s[x1][y1] = "0"
                dq.append([x1, y1])
                cnt += 1
    count.append(cnt)

for i in range(n):
    for j in range(n):
        if s[i][j] == "1":
            bfs(i, j)

count.sort()

print(len(count))
for i in count:
    print(i)