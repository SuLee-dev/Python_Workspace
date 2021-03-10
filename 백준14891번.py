# 톱니바퀴를 방향에 따라 돌리는 함수
def spinning(l, x):
    if (x == 1):
        l.insert(0, l[-1])
        l.pop()
    elif (x == -1):
        l.append(l[0])
        l.remove(l[0])
    return l

# 톱니바퀴 4개 입력 받기
c1 = list(map(int, [i for i in input()]))
c2 = list(map(int, [i for i in input()]))
c3 = list(map(int, [i for i in input()]))
c4 = list(map(int, [i for i in input()]))
li = [c1, c2, c3, c4]


k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    x1, x2 = x, x
    y1, y2 = y, y
    spin = [x] # 돌려야하는 톱니바퀴 저장
    spin_dir = [y] # 각 톱니바퀴의 돌리는 방향 저장
    while x1 > 0: # x의 왼쪽에서 찾기
        if li[x1][-2] == li[x1 - 1][2]:
            break
        else:
            spin.append(x1 - 1)
            y1 *= -1
            spin_dir.append(y1)
        x1 -= 1
    while x2 < 3: # x의 오른쪽에서 찾기
        if li[x2][2] == li[x2 + 1][-2]:
            break
        else:
            spin.append(x2 + 1)
            y2 *= -1
            spin_dir.append(y2)
        x2 += 1
    # print(spin)
    # print(spin_dir)

    for i in range(len(spin)): # 톱니바퀴 돌리기
        li[spin[i]] = spinning(li[spin[i]], spin_dir[i])

# print(li)
# print(li[0][0], li[1][0], li[2][0], li[3][0])

num = 0
for i in range(4):
    num += li[i][0] * 2 ** i


print(num)