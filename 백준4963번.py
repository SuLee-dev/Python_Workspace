from collections import deque

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    s = []
    count = 0

    for i in range(h):
        s.append(list(map(int, input().split())))

    def bfs(a, b):
        global count
        queue = deque([[a, b]])
        s[a][b] = 0
        while queue:
            v = queue.popleft()
            x, y = v[0], v[1]
            for i in range(8):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < h and 0 <= y1 < w and s[x1][y1] == 1:
                    s[x1][y1] = 0
                    queue.append([x1, y1])
        count += 1

    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)

    print(count)
