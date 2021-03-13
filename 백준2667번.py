from collections import deque

# 리스트 내의 "1"이 나오는 첫 위치를 반환하는 함수
def findStart(li, num):
    for i in range(num):
        if (li[i].count("1") > 0):
            x, y = i, li[i].index("1")
            return x, y
    return False

n = int(input())

s = []
for _ in range(n):
    s.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0 # 단지 수

# 리스트 안의 "1"을 해당되는 단지 수로 변환
while True:
    if (findStart(s, n) != False):
        a, b = findStart(s, n)
        cnt += 1
        dq = deque([[a, b]])

        while dq:
            v = dq.popleft()
            x, y = v[0], v[1]

            for i in range(4):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < n and 0 <= y1 < n and s[x1][y1] == "1":
                    s[x1][y1] = cnt
                    dq.append([x1, y1])
    else:
        break

# 리스트를 순회하면서 각 단지 내의 집 개수 세기
ans = [0] * (cnt + 1)
for i in range(n):
    for j in range(n):
        if (type(s[i][j]) == int):
            ans[s[i][j]] += 1

print(cnt)
for i in range(1, cnt + 1):
    print(ans[i])