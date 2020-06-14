def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    pA = sorted(set(A), reverse=True)
    # print(pA)
    cnt = 0
    for i in range(len(pA)-1):
        surplus_cnt = 0
        for j in range(i+1,len(pA)):
            # print(i,j,pA[i],pA[j],cnt)
            if pA[i] % pA[j] == 0:
                surplus_cnt = 0
                break
            else:
                surplus_cnt += 1
        if surplus_cnt > 0:
            cnt += 1
    if len(set(A)) >= 2:
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
