def main():
    N,Y = [int(x) for x in input().split()]
    for x in range(N+1):
        if 10000*x > Y:
            break
        for y in range(N+1):
            if 10000*x+5000*y > Y:
                break
            z = N-(x+y)
            if z < 0 or z > N:
                continue
            # print(x,y,z,Y,10000*x+5000*y+1000*z)
            if Y == 10000*x+5000*y+1000*z:
                print(x,y,z)
                return
    print(-1,-1,-1)

if __name__ == '__main__':
    main()
