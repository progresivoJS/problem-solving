# DP
import sys
read = sys.stdin.readline

def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]

if __name__ == '__main__':
    test = int(read())
    for i in range(test):
        n = int(read())
        a, b = (1, 0), (0, 1)

        if n == 0:
            write("{} {}\n".format(a[0], a[1]))
            continue
        if n == 1:
            write("{} {}\n".format(b[0], b[1]))    
            continue
        
        for j in range(2, n+1):
            a, b = (b), (add_tuple(a, b))
        write("{} {}\n".format(b[0], b[1]))