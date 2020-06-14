def main():
    X = [int(x) for x in input().split()]
    for i,x in enumerate(X):
        if x == 0:
            print(i+1)
            return

if __name__ == '__main__':
    main()
