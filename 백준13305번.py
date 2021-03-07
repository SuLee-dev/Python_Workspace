n = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

temp = price[0]
ans = price[0] * distance[0]

for i in range(1, n - 1):
    temp = temp if temp <= price[i] else price[i]
    ans += temp * distance[i]

print(ans)