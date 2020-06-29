def main():
    E = input().split()
    B = input()
    L = input().split()
    cnt = 0
    bonus = False
    for l in L:
        if l in E:
            cnt += 1
        else:
            if B == l:
                bonus = True
    if cnt == 6:
        print(1)
    elif cnt == 5 and bonus:
        print(2)
    elif cnt == 5:
        print(3)
    elif cnt == 4:
        print(4)
    elif cnt == 3:
        print(5)
    else:
        print(0)

if __name__ == '__main__':
    main()
