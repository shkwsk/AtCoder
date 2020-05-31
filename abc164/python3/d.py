b2019 = [0,1,5,6,7,8,9,10]

def s2019(n):
    ans = 1
    for b in b2019:
        # print(ans)
        ans &= n&2^b
    return ans == 1

def main():
    S = input()
    cnt = 0
    for i in range(len(S)+1):
        for j in range(i+1, len(S)+1):
            # if int(S[i:j]) % 2019 == 0:
            # print(i,j)
            print(i,j,int(S[i:j]),len(bin(int(S[i:j]))))
            if s2019(int(S[i:j])):
                print('####################################################')
                cnt += 1
            # else:
            #     if len(bin(int(S[i:j]))) > 10:
            #         break
    print(cnt)

if __name__ == '__main__':
    main()
