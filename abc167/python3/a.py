def main():
    S = input()
    T = input()
    if S == T[:-1] and len(T) - len(S) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
