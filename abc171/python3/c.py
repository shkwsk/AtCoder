import math

def main():
    N = int(input())
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in range(len(str(N))):
        j = N % 26
        if N == 0:
            break
        if j == 0:
            N = N // 26 - 1
        else:
            N = N // 26
        ans = lowercase[j-1] + ans
        # print(N, j-1, ans)
    print(ans)

if __name__ == '__main__':
    main()
