from collections import defaultdict

def main():
    N = int(input())
    m = defaultdict(int)
    for _ in range(N):
        m[input()] += 1
    print('AC x', m['AC'])
    print('WA x', m['WA'])
    print('TLE x', m['TLE'])
    print('RE x', m['RE'])

if __name__ == '__main__':
    main()
