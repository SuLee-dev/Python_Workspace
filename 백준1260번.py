from collections import deque

# dfs 처리 함수
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#bfs 처리 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for i in range(n + 1)]

# 두 정점을 입력받아 그래프에 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 그래프의 중복된 간선 제거
for i in range(1, len(graph)):
    graph[i] = set(graph[i])
    graph[i] = list(graph[i])
    if i in graph[i]:
        graph[i].remove(i)
    graph[i].sort()


dfs(graph, v, visited)
print()

visited = [False] * (n + 1)
bfs(graph, v, visited)