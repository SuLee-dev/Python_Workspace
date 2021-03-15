from collections import deque

t = int(input())

for _ in range(t):
    
    n = int(input())
    visited = [0] * (n + 1)
    s = [[] for _ in range(n + 1)]
    count = 0

    li = list(map(int, input().split()))
    for i in range(1, n + 1):
        s[i].append(li[i - 1])
        s[li[i - 1]].append(i)

    queue = []
    def dfs(v):
        global visited
        if visited[v] == 0:
            visited[v] = 1
            queue.append(v)
        x = queue[0]
        del queue[0]

        for i in s[x]:
            if visited[i] == 0:
                dfs(i)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            count += 1

    print(count)