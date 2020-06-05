def main():
    N,K = [int(x) for x in input().split()]
    prob = 0
    for i in range(N):
        dice=i+1
        coin = 0
        while dice < K:
            dice *= 2
            coin += 1
        prob += float(1/N) * 0.5**coin
    print(prob)

if __name__ == '__main__':
    main()
