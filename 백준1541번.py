formula = input()

array = formula.split("-")

ans = 0

for i in array[0].split("+"):
    ans += int(i)

for i in range(1, len(array)):
    for j in array[i].split("+"):
        ans -= int(j)

print(ans)