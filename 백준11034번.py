# while True:
#     li = list(map(int, input().split()))
#     cnt = 0
#     while (li[2] - li[0] > 2):
#         if (li[2] - li[1] > li[1] - li[0]):
#             li[0] = li[1] + 1
#         else:
#             li[2] = li[1] - 1
#         li.sort()
#         cnt += 1
#     print(cnt)

while True:
    try:
        a, b, c = map(int, input().split())
        print(max(b - a, c - b) - 1)
    except:
        break