def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input()[::-1])
    for s in sorted(S):
        print(s[::-1])

if __name__ == '__main__':
    main()
