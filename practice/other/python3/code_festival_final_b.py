def main():
    S = input()
    ans = 0
    for i,s in enumerate(S):
        if i%2 == 0:
            ans += int(s)
        else:
            ans -= int(s)
    print(ans)

if __name__ == '__main__':
    main()
