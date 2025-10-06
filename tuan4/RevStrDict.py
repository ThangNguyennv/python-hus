s = input()
a = []
a.extend(s.split())
print({x: x + x[::-1] for x in a})