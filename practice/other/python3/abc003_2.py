def main():
    S = list(input())
    T = list(input())
    AtCoder = ['a','t','c','o','d','e','r']
    win = True
    for s,t in zip(S,T):
        if s == t:
            continue
        if s == '@' and t == '@':
            continue
        if s == '@' and t in AtCoder:
            continue
        if s in AtCoder and t == '@':
            continue
        win = False
    if win:
        print('You can win')
    else:
        print('You will lose')

if __name__ == '__main__':
    main()
