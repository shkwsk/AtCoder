def main():
    S = input()
    n = len(S)
    bit = 0
    total = 0
    ans = ''
    for bit in range(1<<n-1):
        tmp_total = int(S[0])
        ops = ''
        for i in range(n-1):
            if (1<<i) & bit:
                tmp_total += int(S[i+1])
                ops += '+'
            else:
                tmp_total -= int(S[i+1])
                ops += '-'
        if tmp_total == 7:
            ans = S[0]
            for i,op in enumerate(ops):
                ans += op + S[i+1]
            ans += '=7'
    print(ans)

if __name__ == '__main__':
    main()
