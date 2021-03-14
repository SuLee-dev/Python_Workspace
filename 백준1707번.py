from collections import deque

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    color = [0] * (v + 1)
    check = True
    s = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    
    def bfs(v):
        global check, visited, color
        color[v] = 1
        queue = deque([v])

        while queue and check:
            x = queue.popleft()
            y = color[x]

            if visited[x] == 1:
                continue
            visited[x] = 1

            for i in s[x]:
                if visited[i] == 1 and color[x] == color[i]:
                    check = False
                    break
                elif visited[i] == 0:
                    color[i] = -y
                    queue.append(i)

    for i in range(1, v + 1):
        if not check:
            break
        if visited[i] == 0:
            bfs(i)

    if check:
        print("YES")
    else:
        print("NO")