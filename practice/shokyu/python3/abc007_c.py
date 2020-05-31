from collections import defaultdict
import queue

def main():
    R,C = [int(x) for x in input().split()]
    sy,sx = [int(x) for x in input().split()]
    gy,gx = [int(x) for x in input().split()]
    S = []
    for _ in range(R):
        S.append(input())

    # 隣接リスト
    s = (sy-1,sx-1)
    g = (gy-1,gx-1)
    N = defaultdict(list)
    for i in range(R):
        for j in range(C):
            # print(i,j,S[i][j])
            if '#' == S[i][j]:
                continue
            if 0<i and i<R-1:
                if S[i+1][j] != '#':
                    N[(i,j)].append((i+1,j))
                    N[(i+1,j)].append((i,j))
                if S[i-1][j] != '#':
                    N[(i,j)].append((i-1,j))
                    N[(i-1,j)].append((i,j))
            if 0<j and j<C-1:
                if S[i][j+1] != '#':
                    N[(i,j)].append((i,j+1))
                    N[(i,j+1)].append((i,j))
                if S[i][j-1] != '#':
                    N[(i,j)].append((i,j-1))
                    N[(i,j-1)].append((i,j))
            if i==0 and i!=R-1:
                if S[i+1][j] != '#':
                    N[(i,j)].append((i+1,j))
                    N[(i+1,j)].append((i,j))
            elif i!=0 and i==R-1:
                if S[i-1][j] != '#':
                    N[(i,j)].append((i-1,j))
                    N[(i-1,j)].append((i,j))
            if j==0 and j!=C-1:
                if S[i][j+1] != '#':
                    N[(i,j)].append((i,j+1))
                    N[(i,j+1)].append((i,j))
            elif j!=0 and j==C-1:
                if S[i][j-1] != '#':
                    N[(i,j)].append((i,j-1))
                    N[(i,j-1)].append((i,j))
    # print(s)
    # print(g)
    # print(N)

    # bfs
    q = queue.Queue()
    # ステップ数
    V = []
    for _ in range(R):
        V.append([-1]*C)
    V[s[0]][s[1]] = 0
    # 始点
    i,j = s[0],s[1]
    while True:
        for u,v in N[(i,j)]:
            # print(u,v)
            if V[u][v] < 0:
                q.put((u,v))
                V[u][v] = V[i][j]+1 # ステップ数
                # for row in V:
                #     rowstr = ''
                #     for c in row:
                #         if c == -1:
                #             rowstr += ' #'
                #         elif c >= 0:
                #             rowstr += str('%02d' % c)
                #         else:
                #             rowstr += ' .'
                #     print(rowstr)
        if q.empty():
            break
        i,j = q.get()
    # print(V)
    print(V[g[0]][g[1]])
        

if __name__ == '__main__':
    main()
