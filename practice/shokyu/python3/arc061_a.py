def main():
    S = input()
    n = len(S)
    bit = 0
    total = 0
    for bit in range(1<<n-1):
        tmp_total = 0
        tmp = S[0]
        for i in range(n-1):
            # print(bin(bit))
            # print(i, (1<<i) & bit)
            if (1<<i) & bit:
                tmp_total += int(tmp)
                tmp = S[i+1]
            else:
                tmp += S[i+1]
        tmp_total += int(tmp)
        total += tmp_total
    print(total)

if __name__ == '__main__':
    main()
