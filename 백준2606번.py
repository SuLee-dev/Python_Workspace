com = int(input())
line = int(input())

s = [[] for _ in range(com + 1)]
for _ in range(line):
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)
    s[x].append(y)
    s[y].append(x)

visited = [False] * (com + 1)
li = []

def dfs(graph, v, visited):
    visited[v] = True
    li.append(v)
    for i in graph[v]:
        if (visited[i] == False):
            dfs(graph, i, visited)

dfs(s, 1, visited)
print(len(li) - 1)