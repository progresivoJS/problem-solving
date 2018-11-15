import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = [[0 for x in range(3)] for y in range(n)]
    d[0][0] = 0
    d[0][1] = a[0]
    d[0][2] = b[0]
    for i in range(1, n):
        d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
        d[i][1] = max(d[i-1][0] + a[i], d[i-1][2] + a[i])
        d[i][2] = max(d[i-1][0] + b[i], d[i-1][1] + b[i])
    
    print(max(d[n-1]))