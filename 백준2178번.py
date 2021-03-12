from collections import deque

n, m = map(int, input().split())

# n x m 크기의 미로 생성
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

cnt = 0
queue = deque([1])
visited = [False for _ in range(n * m + 1)]

# n x m 에 도착할때까지 BFS로 길 찾기
while queue:
    v = queue.popleft()
    length = len(queue)
    visited[v] = True
    cnt += 1
    x = (v - 1) // m
    y = (v - 1) % m
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    changed = False
    for i in range(4):
        if (x + dir[i][0] >= n or x + dir[i][0] < 0 or y + dir[i][1] >= m or y + dir[i][1] < 0):
            continue
        else:
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            num = dx * m + (dy + 1)
            if visited[num] == False and miro[dx][dy] == 1:
                visited[num] = True
                queue.append(num)
                changed = True

    # 그전의 큐와 비교했을 때 겹치는 요소가 있어도 원소의 개수가 변경될 경우 -1
    if (changed and length >= 1):
        cnt -=1
 
    print(queue)

print(cnt)