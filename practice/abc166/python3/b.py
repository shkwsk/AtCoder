def main():
    N,K = [int(x) for x in input().split()]
    snack_sunuke = []
    for a in range(K):
        di = int(input())
        for i in [int(x) for x in input().split()]:
            snack_sunuke.append(i)
    print(N - len(set(snack_sunuke)))

if __name__ == '__main__':
    main()
