def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort(reverse=True)
    print(sum(A[0::2]) - sum(A[1::2]))

if __name__ == '__main__':
    main()
