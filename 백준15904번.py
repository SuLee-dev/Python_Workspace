string = input()
UCPC = "UCPC"
cnt = 0
for i in string:
    if (i == UCPC[cnt]):
        cnt += 1
    if cnt == 4 : break

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")