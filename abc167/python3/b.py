def main():
    A,B,C,K = [int(x) for x in input().split()]
    v = 0
    if A<K:
        K -= A
        v += A*1
    else:
        v += K*1
        print(v)
        return
    if B<K:
        K -= B
        v += B*0
    else:
        v += K*0
        print(v)
        return
    if C<K:
        K -= C
        v += C*(-1)
    else:
        v += K*(-1)
        print(v)

if __name__ == '__main__':
    main()
