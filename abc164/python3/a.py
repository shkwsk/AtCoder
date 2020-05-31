def main():
    S,W = [int(x) for x in input().split()]
    if W >= S:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()
