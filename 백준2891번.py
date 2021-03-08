n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
spare = list(map(int, input().split()))
li = [1] * n

for i in damaged:
    li[i - 1] -= 1
for i in spare:
    li[i - 1] += 1

# print(li)

if li[0] == 0 and li[1] == 2:
    li[0], li[1] = 1, 1
if li[n - 1] == 0 and li[n - 2] == 2:
    li[n - 1], li[n - 2] = 1, 1

# print(li)

for i in range(1, n - 1):
    if (li[i] == 0):
        if (li[i - 1] == 2):
            li[i - 1] -= 1
            li[i] += 1
        elif (li[i + 1] == 2):
            li[i + 1] -= 1
            li[i] += 1

# print(li)
print(li.count(0))