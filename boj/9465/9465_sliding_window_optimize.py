import sys
input = open('/Users/Mac/repos/problem-solving/data/data.txt').readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x, y, z = 0, 0, 0
    for i in range(n):
        x, y, z = max(x, y, z), max(x, z) + a[i], max(x, y) + b[i]
    
    print(max(x, y, z))