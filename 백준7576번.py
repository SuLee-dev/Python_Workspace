from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
s = []

for _ in range(n):
    s.append(list(input().split()))

queue = deque()
for i in range(n):
    for j in range(m):
        if s[i][j] == "1":
            s[i][j] = 0
            queue.append([i, j])

def bfs():
    
    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < n and 0 <= y1 < m:
                if s[x1][y1] == "0":
                    queue.append([x1, y1])
                    s[x1][y1] = s[x][y] + 1
                elif type(s[x1][y1]) == int and s[x1][y1] > s[x][y] + 1:
                    queue.append([x1, y1])
                    s[x1][y1] = s[x][y] + 1

check = False
num = 0

bfs()
for i in range(n):
    for j in range(m):
        if s[i][j] == "0":
            check = True
        if type(s[i][j]) == int:
            num = max(num, s[i][j])

if check:
    print(-1)
else:
    print(num)