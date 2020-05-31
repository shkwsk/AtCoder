from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(V,N,g,i,j,goal):
    # print('============')
    # print(i,j)
    if g == (i,j):
        goal = True
        return V,goal
    V[i][j] = 1
    for u,v in N[(i,j)]:
        # print(str(i),str(j),'->',str(u),str(v))
        if V[u][v] >= 0:
            # print('skip',str(u),str(v))
            continue
        V,goal = dfs(V,N,g,u,v,goal)
        if goal:
            break
    return V,goal

def main():
    H,W = [int(x) for x in input().split()]
    C = []
    for _ in range(H):
        C.append(input())

    # 隣接リスト
    s = (0,0)
    g = (0,0)
    N = defaultdict(list)
    for i in range(H):
        for j in range(W):
            # print(i,j)
            if '#' == C[i][j]:
                continue
            if 's' == C[i][j]:
                s = (i,j)
            if 'g' == C[i][j]:
                g = (i,j)
            if 0<i and i<H-1:
                if C[i+1][j] != '#':
                    N[(i,j)].append((i+1,j))
                    # print('down')
                if C[i-1][j] != '#':
                    N[(i,j)].append((i-1,j))
                    # print('up')
            if 0<j and j<W-1:
                if C[i][j+1] != '#':
                    N[(i,j)].append((i,j+1))
                    # print('right')
                if C[i][j-1] != '#':
                    N[(i,j)].append((i,j-1))
                    # print('left')
            if i==0 and i!=H-1:
                if C[i+1][j] != '#':
                    N[(i,j)].append((i+1,j))
                    # print('down')
            elif i!=0 and i==H-1:
                if C[i-1][j] != '#':
                    N[(i,j)].append((i-1,j))
                    # print('up')
            if j==0 and j!=W-1:
                if C[i][j+1] != '#':
                    N[(i,j)].append((i,j+1))
                    # print('right')
            elif j!=0 and j==W-1:
                if C[i][j-1] != '#':
                    N[(i,j)].append((i,j-1))
                    # print('left')
    # print(s)
    # print(g)
    # print(N)

    # 訪問行列 ([[-1]*W]*H だと参照もコピーされてしまうのでappendする)
    V = []
    for _ in range(H):
        V.append([-1]*W)
    V,goal = dfs(V,N,g,s[0],s[1],False)
    if goal:
        print('Yes')
    else:
        print('No')
        

if __name__ == '__main__':
    main()
