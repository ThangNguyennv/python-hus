s = input()
a = []
a.extend(s.split(','))
l = []
for x in a:
    l.append(int(x, 2))
print(l)
k = []
for x in l:
    if x % 5 == 0:
        k.append(x)
m = []
for x in k:
    m.append(bin(x)[2:].zfill(4))
print(','.join(m))
