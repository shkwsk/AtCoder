def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    C = 1000
    for i in range(N - 1):
        if A[i] < A[i + 1]:
            b = C // A[i]
            # print(b)
            C -= A[i] * b
            # print(C)
            C += A[i + 1] * b
            # print(C)
    print(C)


if __name__ == "__main__":
    solve()