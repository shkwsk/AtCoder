def main():
    N = int(input())
    D = list(set([int(input()) for x in range(N)]))
    D.sort(reverse=True)
    print(len(D))

if __name__ == '__main__':
    main()
