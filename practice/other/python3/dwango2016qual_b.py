def main():
    N = int(input())
    K = [int(x) for x in input().split()]
    ans = [-1]*N
    for i in range(len(K)-1):
        if K[i] > K[i+1]:
            if ans[i] < 0:
                ans[i] = K[i]
            ans[i+1] = K[i+1]
            ans[i+2] = K[i+1]
        elif K[i] < K[i+1]:
            if ans[i] < 0:
                ans[i] = K[i]
            ans[i+1] = K[i]
            ans[i+2] = K[i+1]
        else:
            if ans[i+1] < 0:
                ans[i+1] = K[i+1]
            if i == 0:
                ans[0] = K[i]
            if i+2 == N-1:
                ans[N-1] = K[i+1]
    print(' '.join([str(a) for a in ans]))

if __name__ == '__main__':
    main()
