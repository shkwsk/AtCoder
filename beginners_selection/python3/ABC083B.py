def main():
    N,a,b = [int(x) for x in input().split()]
    ans = 0
    for n in range(N+1):
        digitsum = sum([int(s) for s in str(n)])
        if a <= digitsum and digitsum <= b:
            ans += n
    print(ans)

if __name__ == '__main__':
    main()
