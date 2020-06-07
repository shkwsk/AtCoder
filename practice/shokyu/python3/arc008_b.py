from collections import defaultdict
import copy

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
    kit = []
    kanban = ''
    kanban_dict = defaultdict(int)
    while ''.join(name) != kanban and len(name) >= len(kanban):
        kit += masterkit
        cnt += 1
        for n in name:
            if n in kit and name_dict[n] > kanban_dict[n]:
                c = kit.pop(kit.index(n))
                kanban += c
                kanban_dict[c] += 1
    print(cnt)

if __name__ == '__main__':
    main()
