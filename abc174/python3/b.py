import math


def solve():
    N, D = [int(x) for x in input().split()]
    ans = 0
    for _ in range(N):
        X, Y = [int(x) for x in input().split()]
        if math.sqrt(X**2 + Y**2) <= D:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()