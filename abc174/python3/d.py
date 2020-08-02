def solve():
    N = int(input())
    C = input()
    i = 0
    j = N - 1
    ans = 0
    while i < j:
        if C[i] == 'W' and C[j] == 'W':
            j -= 1
        elif C[i] == 'W' and C[j] == 'R':
            i += 1
            j -= 1
            ans += 1
        elif C[i] == 'R' and C[j] == 'R':
            i += 1
        elif C[i] == 'R' and C[j] == 'W':
            i += 1
            j -= 1
    print(ans)


if __name__ == "__main__":
    solve()