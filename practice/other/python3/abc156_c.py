def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    avgX = round(sum(X) / len(X))
    diff = 0
    for i in range(N):
        diff += (X[i] - avgX)**2
    print(diff)

if __name__ == '__main__':
    main()
