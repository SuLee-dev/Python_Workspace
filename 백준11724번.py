n, m = map(int, input().split())
s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

visited = [0] * (n + 1)

cnt = 0

def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and s[v][i] == 1:
            dfs(i)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)