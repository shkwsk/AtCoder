def main():
    X,Y = [int(x) for x in input().split()]
    tsuru = 2
    kame = 4
    for i in range(X+1):
        if Y == (X-i)*kame + i*tsuru:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
