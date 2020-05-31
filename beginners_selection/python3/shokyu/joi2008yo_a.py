def main():
    N = int(input())
    change = 1000-N
    cnt = 0
    while change >= 500:
        change -= 500
        cnt += 1
    while change >= 100:
        change -= 100
        cnt += 1
    while change >= 50:
        change -= 50
        cnt += 1
    while change >= 10:
        change -= 10
        cnt += 1
    while change >= 5:
        change -= 5
        cnt += 1
    while change >= 1:
        change -= 1
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
