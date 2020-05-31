def main():
    A,B = [x for x in input().split()]
    print(int(A)*round(float(B)*100)//100)

if __name__ == '__main__':
    main()
