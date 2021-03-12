from collections import deque

n, m = map(int, input().split())

# n x m 크기의 미로 생성
miro = []
for i in range(n):
    miro.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# n x m 에 도착할때까지 BFS로 길 찾기
miro[0][0] = 1
queue = [[0, 0]]

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and miro[x][y] == "1":
            queue.append([x, y])
            miro[x][y] = miro[a][b] + 1

print(miro[n - 1][m - 1])