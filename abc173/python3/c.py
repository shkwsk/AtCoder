def main():
    H,W,K = [int(x) for x in input().split()]

    B = 0
    BH = [0]*H
    BW = [0]*W
    BHW = []
    for h in range(H):
        BHW.append([0]*W)
    for i in range(H):
        C = list(input())
        for j in range(W):
            if C[j] == '#':
                B += 1
                BH[i] += 1
                BW[j] += 1
                BHW[i][j] = 1

    cnt = 0
    for ibit in range(0,1<<H):
        for jbit in range(0,1<<W):
            icost = 0
            jcost = 0
            ijcost = 0
            for i in range(H):
                if (1<<i) & ibit:
                    icost += BH[i]
            for j in range(W):
                if (1<<j) & jbit:
                    jcost += BW[j]
            for i in range(H):
                for j in range(W):
                    if (1<<i) & ibit and (1<<j) & jbit:
                        ijcost += BHW[i][j]
            b = B - icost - jcost + ijcost
            if K == b:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
