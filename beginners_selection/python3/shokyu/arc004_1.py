import math

def main():
    N = int(input())
    x_min,x_max,y_min,y_max = 100,0,100,0
    xl,yl = [],[]
    for i in range(N):
        x,y = [int(x) for x in input().split()]
        xl.append(x)
        yl.append(y)

    D = []
    for x1,y1 in zip(xl,yl):
        for x2,y2 in zip(xl,yl):
            D.append(math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2))
    print(max(D))

if __name__ == '__main__':
    main()
