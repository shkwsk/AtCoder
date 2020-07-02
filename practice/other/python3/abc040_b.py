def main():
    n = int(input())
    N = 100000
    ans = 100000
    for i in range(1,N):
        for j in range(i,N):
            if n < i*j:
                break
            a = n-i*j + j-i
            if a < ans:
                ans = a
    print(ans)

if __name__ == '__main__':
    main()
