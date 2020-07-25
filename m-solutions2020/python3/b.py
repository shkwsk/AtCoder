def solve():
    A, B, C = [int(x) for x in input().split()]
    K = int(input())
    ans = False
    for i in range(K):
        red = A * 2**i
        green = B * 2**(K - i)
        blue = C
        # print(i, red, green, blue)
        if green > red and blue > green:
            ans = True
            break

        red = A
        green = B * 2**i
        blue = C * 2**(K - i)
        # print(i, red, green, blue)
        if green > red and blue > green:
            ans = True
            break

        red = A * 2**i
        green = B
        blue = C * 2**(K - i)
        # print(i, red, green, blue)
        if green > red and blue > green:
            ans = True
            break

    if ans:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()