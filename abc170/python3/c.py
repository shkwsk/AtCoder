def main():
    X,N = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    top_diff = 200
    ans = 0
    for i in range(-101,201):
        # print(i,top_diff,ans)
        if not i in P:
            if abs(X-i) < top_diff:
                top_diff = X-i
                ans = i
    print(ans)

if __name__ == '__main__':
    main()
