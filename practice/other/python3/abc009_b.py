def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    max_price = max(A)
    for a in sorted(A, reverse=True):
        if a == max_price:
            continue
        else:
            print(a)
            return

if __name__ == '__main__':
    main()
