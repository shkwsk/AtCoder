from collections import defaultdict

def main():
    N,M = [int(x) for x in input().split()]
    pl = defaultdict(list)
    for i in range(M):
        x,y = [int(x) for x in input().split()]
        pl[x].append(y)
    ll = {}
    for k,v in pl.items():
        ll.update({k:len(v)})
    if len(ll) == 0:
        print(1)
    else:
        print(sorted(ll.items(),key=lambda x:x[1],reverse=True)[0][1]+1)

if __name__ == '__main__':
    main()
