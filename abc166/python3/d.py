def main():
    X = int(input())
    A = 0
    B = 0
    while True:
        A += 1
        for B in reversed(range(A*(-1)+1,A)):
            # print(A**5 - B**5)
            if A**5 - B**5 == X:
                print(A,B)
                return

if __name__ == '__main__':
    main()
