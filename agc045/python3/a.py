def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        S = [int(x) for x in list(input())]
        length = 0
        statuses = [0,0]
        status = 0
        # print('=======================')
        turn = 0
        while len(S) > 0:
            # 連続ターン数を数える
            turn_count = turn
            s = S[0]
            while len(S) > 0:
                _s = S[0]
                if s == _s:
                    S.pop(0)
                    turn_count += 1
                else:
                    break
            # 人が最適にxorした値を更新
            # print('###')
            # print(turn_count)
            turn_values = list(set(A[turn:turn_count]))
            for bit in range(1,2**len(turn_values)):
                # print(bin(bit),turn_values)
                totalA = status
                for i,v in enumerate(turn_values):
                    if (1<<i) & bit:
                        totalA ^= v
                    # print((1<<i) & bit,totalA,v)
                # print(totalA)
                if s == 1 and status < totalA:
                    status = totalA
                elif s == 0 and status > totalA:
                    status = totalA
            # print(status)
            turn += turn_count
        ans.append(status)

    # print('############################')
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
