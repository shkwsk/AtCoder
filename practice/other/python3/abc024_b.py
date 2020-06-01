def main():
    N,T = [int(x) for x in input().split()]
    A = []
    for _ in range(N):
        A.append(int(input()))
    time = 0
    for i in range(N-1):
        # print(A[i],A[i+1],time)
        if A[i]+T < A[i+1]:
            time += T
        else:
            time += A[i+1] - A[i]
    print(time+T)

if __name__ == '__main__':
    main()
