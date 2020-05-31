def f(N,Y):
    for i in range(N+1):
        for j in range(N+1):
            k=N-i-j
            if k < 0:
                break
            if i+j+k == N and 10000*i + 5000*j + 1000*k == Y:
                x,y,z = i,j,k
                return x,y,z
    return -1,-1,-1

def main():
    N,Y = [int(x) for x in input().split()]
    x,y,z = f(N,Y)
    print(x,y,z)

if __name__ == '__main__':
    main()
