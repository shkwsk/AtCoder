from collections import defaultdict
import itertools

def main():
    N,M = [int(x) for x in input().split()]
    room = defaultdict(int)
    for x in input().split():
        room[int(x)] += 1
    resv = defaultdict(int)
    for x in input().split():
        resv[int(x)] += 1

    for i in range(1,100000):
        # print(resv[i], room[i], resv[i] - room[i])
        resv[i+1] += max(0,resv[i] - room[i])
    if resv[100000] <= room[100000]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
