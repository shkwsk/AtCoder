from collections import defaultdict

def main():
    N = int(input())
    A = input().split()
    counts = defaultdict(int)
    ans = 0
    for a in A:
        counts[a] += 1
        ans += int(a)
    Q = int(input())
    BC = []
    for _ in range(Q):
        BC.append(input().split())
    for b,c in BC:
        ans += (int(c)-int(b)) * counts[b]
        print(ans)
        counts[c] += counts[b]
        counts[b] = 0

if __name__ == '__main__':
    main()
