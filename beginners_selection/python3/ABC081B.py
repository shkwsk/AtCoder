def div2IfAllEven(A, divnum):
    is_even = True
    for a in A:
        if a % 2:
            is_even = False
    if is_even:
        divnum += 1
        return div2IfAllEven([a/2 for a in A], divnum)
    return A, divnum

def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    divnum = 0
    A, divnum = div2IfAllEven(A, divnum)
    print(divnum)

if __name__ == '__main__':
    main()
