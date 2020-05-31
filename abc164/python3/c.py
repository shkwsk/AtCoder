def main():
    N = int(input())
    S = {}
    for i in range(N):
        s = input()
        if s not in S:
            S.update({s:0})
    print(len(S))

if __name__ == '__main__':
    main()
