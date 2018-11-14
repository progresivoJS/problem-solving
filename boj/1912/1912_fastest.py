n = input()
a = list(map(int, input().split()))

s = 0
r = -1000
for x in a:
    s += x
    r = max(r, s)
    s = max(s, 0)
print(r)