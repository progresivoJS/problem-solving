import sys
read = sys.stdin.readline

if __name__ == "__main__":
    n = int(read())
    f = [0, 0]
    for i in range(2, n+1):
        result = 1 + f[i-1]
        if i % 2 == 0:
            result = min(result, 1 + f[i//2])
        if i % 3 == 0:
            result = min(result, 1 + f[i//3])
        f.append(result)
    print(f[n])