def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    SA = sorted(A, reverse=True)
    ans = 0
    for i in range(1,len(SA)):
        ans += SA[i-1]
    print(ans)

if __name__ == '__main__':
    main()
