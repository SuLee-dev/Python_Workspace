import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    li = []
    ans = 0
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        li.append((a, b))

    li = sorted(li, key = lambda x : (x[0], x[1]))

    cnt = 1
    temp = li[0]
    for i in range(1, n):
        if(li[i][1] <= temp[1]):
            cnt += 1
            temp = li[i]
            

    print(cnt)