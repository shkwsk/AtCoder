def main():
    N,M = [int(x) for x in input().split()]
    Scc_cnt = 0
    if N >= 0 and M >= 2:
        if M >= N*2:
            Scc_cnt += N + (M-N*2)//4
        else:
            Scc_cnt += M//2
    print(Scc_cnt)

if __name__ == '__main__':
    main()
