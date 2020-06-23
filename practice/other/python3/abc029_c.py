import itertools

def main():
    N = int(input())
    phrase = ['a','b','c']
    for p in itertools.product(phrase, repeat=N):
        print(''.join(p))

if __name__ == '__main__':
    main()
