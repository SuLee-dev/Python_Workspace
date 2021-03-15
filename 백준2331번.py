a, p = map(int, input().split())
li = [a]

def rp(v):
    global li, p
    v = str(v)
    num = 0
    for i in v:
        num += int(i) ** p
    if num not in li:
        li.append(num)
        rp(num)
    else:
        index = li.index(num)
        del li[index:]
        return False

rp(a)
print(len(li))