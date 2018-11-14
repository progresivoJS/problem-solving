def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]

if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        n = int(input())
        zero = (1, 0), one = (0, 1)
        for j in range(2, n+1):
            d.append(add_tuple(d[j-2], d[j-1]))
        print("{} {}".format(d[n][0], d[n][1]))