# import math

# def lcm(x, y):
#     return (x * y) // math.gcd(x, y)

# def main():
#     A,V = [int(x) for x in input().split()]
#     B,W = [int(x) for x in input().split()]
#     T = int(input())
#     pA = A + V*T
#     pB = B + W*T
#     lcm = lcm(A,B))
#     if pA >= pB:
#         print('YES')
#     else:
#         print('NO')

def main():
    A,V = [int(x) for x in input().split()]
    B,W = [int(x) for x in input().split()]
    T = int(input())
    pA = A
    pB = B
    if pA > pB:
        print('NO')
        return
    for _ in range(T):
        if pA <= pB and pB+W <= pA+V:
            print('YES')
            return
        pA += V
        pB += W
    print('NO')

if __name__ == '__main__':
    main()
