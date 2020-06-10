from collections import defaultdict

def main():
    N = int(input())
    S = defaultdict(int)
    for i in range(N):
        s = input()
        S[s] += 1
    max_cnt = max(S.values())
    ans = []
    for k,v in sorted(S.items(), key=lambda x:x[1], reverse=True):
        if v == max_cnt:
            ans.append(k)
        else:
            break
    for a in sorted(ans):
        print(a)

if __name__ == '__main__':
    main()
 
