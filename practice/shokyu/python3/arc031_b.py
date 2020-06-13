from collections import defaultdict
import copy
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(V,nl,i,j,cnt):
    V[i][j] = 1
    cnt += 1
    for u,v in nl[(i,j)]:
        if V[u][v] >= 0:
            continue
        V,cnt = dfs(V,nl,u,v,cnt)
    return V,cnt

def make_nl(A):
    nl = defaultdict(list)
    for i in range(10):
        for j in range(10):
            if 'x' == A[i][j]:
                continue
            if 0<i and i<9:
                if A[i+1][j] == 'o':
                    nl[(i,j)].append((i+1,j))
                if A[i-1][j] == 'o':
                    nl[(i,j)].append((i-1,j))
            if 0<j and j<9:
                if A[i][j+1] == 'o':
                    nl[(i,j)].append((i,j+1))
                if A[i][j-1] == 'o':
                    nl[(i,j)].append((i,j-1))
            if i==0 and i!=9:
                if A[i+1][j] == 'o':
                    nl[(i,j)].append((i+1,j))
            elif i!=0 and i==9:
                if A[i-1][j] == 'o':
                    nl[(i,j)].append((i-1,j))
            if j==0 and j!=9:
                if A[i][j+1] == 'o':
                    nl[(i,j)].append((i,j+1))
            elif j!=0 and j==9:
                if A[i][j-1] == 'o':
                    nl[(i,j)].append((i,j-1))
    return nl

def main():
    A = []
    o_cnt = 0
    s = (-1,-1)
    for i in range(10):
        al = list(input())
        o_cnt += al.count('o')
        A.append(al)
        if s[0] >= 0 and s[1] >= 0:
            continue
        try:
            j = al.index('o')
            s = (i,j)
        except:
            continue
    # print(A)
    # print(s)
    # print(o_cnt)

    for i in range(10):
        for j in range(10):
            if A[i][j] == 'o':
                continue
            else:
                tmpA = copy.copy(A)
                tmpA[i][j] = 'o'
                nl = make_nl(tmpA)
                # print(nl)
                V = []
                for _ in range(10):
                    V.append([-1]*10)
                V,cnt = dfs(V,nl,s[0],s[1],0)
                # print(i,j)
                # print(tmpA)
                # print(cnt)
                tmpA[i][j] = 'x'
                if cnt == o_cnt+1:
                    print('YES')
                    return
    print('NO')
                

if __name__ == '__main__':
    main()
