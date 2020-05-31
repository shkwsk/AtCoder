import numpy as np

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    # print(P)

    dp = np.zeros((N+1,sum(P)+1))
    for i in range(N):
        for j in range(sum(P)+1):
            # print(i,j)
            if j < P[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-P[i]]+P[i])
            # print(dp)
    # print(np.unique(dp))
    print(len(np.unique(dp)))
        

if __name__ == '__main__':
    main()
