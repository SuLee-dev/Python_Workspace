t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    visited = [0] * (n + 1)
    s = [0]
    li = list(map(int, input().split()))
    for i in range(1, n + 1):
        s.append(li[i - 1])

    def dfs(v):
        global count
        queue.append(v)
        visited[v] = 1
        if s[v] == v:
            queue.pop()

        if visited[s[v]] == 0:
            dfs(s[v])
        else:
            if queue:
                temp = 0
                for i in range(len(queue)):
                    if queue[i] != s[v]:
                        temp += 1
                    else:
                        count += temp
                        return
            count += len(queue)
            return


    for i in range(1, n + 1):
        queue = []
        if visited[i] == 0:
            dfs(i)

    print(count)