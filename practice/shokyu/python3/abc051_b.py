def main():
    K,S = [int(x) for x in input().split()]
    cnt = 0
    for x in range(K+1):
        if x > S:
            break
        for y in range(K+1):
            if x+y > S:
                break
            z = S-(x+y)
            if z < 0 or z > K:
                continue
            # print(x,y,z)
            if S == x+y+z:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
