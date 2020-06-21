def main():
    N,K = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    ans = 0
    for i,p in enumerate(sorted(P)):
        if i == K:
            break
        ans += p
    print(ans)

if __name__ == '__main__':
    main()
