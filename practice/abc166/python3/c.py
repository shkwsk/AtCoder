from collections import defaultdict

def main():
    N,M = [int(x) for x in input().split()]
    Hl = [int(x) for x in input().split()]
    Al,Bl = [],[]
    for i in range(M):
        A,B = [int(x) for x in input().split()]
        Al.append(A)
        Bl.append(B)

    is_peek = [1]*N
    m = defaultdict(list)
    for A,B in zip(Al,Bl):
        if Hl[A-1] > Hl[B-1]:
            is_peek[B-1] = 0
        elif Hl[A-1] == Hl[B-1]:
            is_peek[A-1] = 0
            is_peek[B-1] = 0
        else:
            is_peek[A-1] = 0
    print(sum(is_peek))
        

if __name__ == '__main__':
    main()
