s = input()

s0 = s.replace("0", " ")
s1 = s.replace("1", " ")

li_s0 = list(s0.split())
li_s1 = list(s1.split())

print(min(len(li_s0), len(li_s1)))