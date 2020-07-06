def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    for i in range(N):
        ans = ''
        for s in reversed(S):
            ans += s[i]
        print(ans)

if __name__ == '__main__':
    main()
