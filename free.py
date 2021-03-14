n, m, v = map(int, input().split())
visited = [0 for _ in range(n + 1)]
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(v):
    visited[v] = 1
    print(v, end = " ")
    for i in range(1, n + 1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = 0
    queue = [v]
    while queue:
        v = queue[0]
        print(v, end = " ")
        del queue[0]
        for i in range(1, n + 1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)