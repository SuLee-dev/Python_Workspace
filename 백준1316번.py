n = int(input())
li = []
cnt = n

for _ in range(n):
    li.append(input())


for i in range(n):
    word = li[i]
    temp = [word[0]]
    length = len(word)
    if length >= 2:
        for j in range(1, length):
            temp.append(word[j])
            if (temp[-2] != word[j] and word[j] in temp[:j]):
                cnt -= 1
                break

print(cnt)