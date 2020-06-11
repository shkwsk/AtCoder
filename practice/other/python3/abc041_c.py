def main():
    N = int(input())
    A = {}
    for i,a in enumerate(input().split()):
        A.update({i+1:int(a)})
    for i,a in sorted(A.items(), key=lambda x:x[1], reverse=True):
        print(i)

if __name__ == '__main__':
    main()
