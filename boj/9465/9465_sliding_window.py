import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x, y, z = 0, a[0], b[0]
    for i in range(1, n):
        x, y, z = max(x, y, z), max(x + a[i], z + a[i]), max(x + b[i], y + b[i])
    
    print(max(x, y, z))