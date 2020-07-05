def main():
    N = int(input())
    a = N % 1000
    while N > 0:
        N -= 1000
    print(-N)

if __name__ == '__main__':
    main()
