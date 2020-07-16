def main():
    a,b = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    R = []
    for i in range(10):
        if i in P:
            R.append('.')
        elif i in Q:
            R.append('o')
        else:
            R.append('x')
    print(' '.join(R[7:10] + [R[0]]))
    print(' ' + ' '.join(R[4:7]))
    print('  ' + ' '.join(R[2:4]))
    print('   ' + R[1])

if __name__ == '__main__':
    main()
