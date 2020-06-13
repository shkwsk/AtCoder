import copy

def main():
    N,K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    for k in range(K):
        nextA = [1]*N
        for i in range(N):
            # print(max(0,i-A[i]),min(i+A[i],N))
            for j in range(max(0,i-A[i]),min(i+A[i]+1,N)):
                if i == j:
                    continue
                nextA[j] += 1
                # print(i,j,A[i],nextA)
        A = copy.copy(nextA)
        flag = True
        for i in range(N):
            if A[i] < N:
                flag = False
        if flag:
            for i in range(N):
                nextA = A[i] + (N-k)
            break
    print(' '.join([str(a) for a in nextA]))

if __name__ == '__main__':
    main()
