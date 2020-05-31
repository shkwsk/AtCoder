import numpy as np

def main():
    N,D = [int(x) for x in input().split()]
    # print(P)
    dice = [1,2,3,4,5,6]

    dp = np.zeros((N+1,6**D+1))
    for i in range(N):
        for j in range(sum(P)+1):
            # print(i,j)
            if j < P[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-dice[i]]+dice[i])
            # print(dp)
    # print(np.unique(dp))
    print(len(np.unique(dp)))
        

if __name__ == '__main__':
    main()
