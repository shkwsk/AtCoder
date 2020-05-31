def main():
    N,M,X = [int(x) for x in input().split()]
    Cl,All = [],[]
    for i in range(N):
        tmp = [int(x) for x in input().split()]
        Cl.append(tmp[0])
        All.append((tmp[1:]))
    # print(Cl)
    # print(All)
    min_cost = sum(Cl) + 1
    for bit in range(1,1<<N):
        # print(bin(bit))
        cost = 0
        totalAl = [0]*M
        for i,al in enumerate(All):
            if (1<<i) & bit:
                # print(i)
                for j,a in enumerate(al):
                    totalAl[j] += a
                cost += Cl[i]
        check = True
        for a in totalAl:
            if a < X:
                check = False
        if check:
            min_cost = min(min_cost, cost)
    if min_cost > sum(Cl):
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()
