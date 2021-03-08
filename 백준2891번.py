n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
spare = list(map(int, input().split()))
li = [1] * n

for i in damaged:
    li[i - 1] -= 1
for i in spare:
    li[i - 1] += 1

print(li)



print(li.count(0))