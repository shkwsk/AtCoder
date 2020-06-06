from collections import defaultdict

def main():
    N = int(input())
    town = defaultdict(int)
    for _ in range(N):
        s,p = input().split()
        town[s] = int(p)
    sumpeople = sum(town.values())
    top_town = sorted(town.items(),key=lambda x:x[1],reverse=True)[0]
    # print(sumpeople,top_town)
    if sumpeople & 2 == 1:
        if top_town[1] > sumpeople//2+1:
            print(top_town[0])
            return
    else:
        if top_town[1] > sumpeople//2:
            print(top_town[0])
            return
    print('atcoder')

if __name__ == '__main__':
    main()
