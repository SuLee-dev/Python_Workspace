n = int(input())
a, b, c, d, e, f = map(int, input().split())
dice = [a, b, c, d, e, f]
li = [min(a, f), min(b, e), min(c, d)]
li.sort()

if (n == 1):
    ans = sum(dice) - max(dice)
else:
    ans = sum(li) * 8 + (li[0] + li[1]) * (n - 2) * 12 + li[0] * (n - 2) ** 2 * 6
    ans -= li[2] * 4 + li[1] * (n - 2) * 4 + li[0] * (n - 2) ** 2
print(ans)