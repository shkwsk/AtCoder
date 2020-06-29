def main():
    D = int(input())
    C = [int(x) for x in input().split()]
    S = []
    total_s = [0]*26
    for _ in range(D):
        s = [abs(int(x)) for x in input().split()]
        # for j in s:
        #     total_s[]
        S.append(s)
    
    for i in range(D):
        print(S[i].index(max(S[i]))+1)

if __name__ == '__main__':
    main()
