def main():
    a,b = input().split()
    if (int(a) * int(b)) % 2:
        print('Odd')
    else:
        print('Even')

if __name__ == '__main__':
    main()
