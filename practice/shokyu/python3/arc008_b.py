from collections import defaultdict
import math

def main():
    N,M = [int(x) for x in input().split()]
    name = list(input())
    name_dict = defaultdict(int)
    for n in name:
        name_dict[n] += 1
    masterkit = list(input())
    masterkit_dict = defaultdict(int)
    for n in masterkit:
        masterkit_dict[n] += 1

    for n in name:
        if not n in masterkit_dict:
            print(-1)
            return

    cnt = 0
    for k,v in name_dict.items():
        kit_cnt = masterkit_dict[k]
        cnt = max(cnt, math.ceil(v / kit_cnt))
    print(cnt)

if __name__ == '__main__':
    main()
