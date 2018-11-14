import sys
read = sys.stdin.readline
n = int(read())
a = list(map(int, (read().split())))

d = [a[0]]
for i in range(1, n):
    d.append(max(a[i], d[i-1] + a[i]))

print(max(d))