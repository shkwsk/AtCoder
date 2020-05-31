def main():
    N = int(input())
    tl = []
    for i in range(N):
        tl.append(int(input()))
    yl=[0]*2
    for t in sorted(tl, reverse=True):
        yl[yl.index(min(yl))] += t
    print(max(yl))

if __name__ == '__main__':
    main()
