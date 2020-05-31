import math
from collections import defaultdict

def main():
    N = int(input())
    Al = [int(x) for x in input().split()]
    center = int(N/2)
    cnt = 0
    m = defaultdict(int)
    for i in range(N):
        m[i+Al[i]] += 1
        cnt += m[i-Al[i]]
    print(cnt)

if __name__ == '__main__':
    main()
