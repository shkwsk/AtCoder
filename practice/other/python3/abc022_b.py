from collections import defaultdict

def main():
    N = int(input())
    A = defaultdict(int)
    cnt = 0
    for _ in range(N):
        a = int(input())
        if A[a] > 0:
            cnt += 1
        A[a] += 1
    print(cnt)

if __name__ == '__main__':
    main()
