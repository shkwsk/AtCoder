def main():
    A = list('123456')
    N = int(input())
    a = N % 30
    b = a // 5
    c = a % 5
    B = A[b:] + A[:b]
    for i in range(c):
        B[i], B[i+1] = B[i+1], B[i]
    print(''.join(B))

if __name__ == '__main__':
    main()
