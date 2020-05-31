import sys
sys.setrecursionlimit(1000)

def f(S):
    if S == 'dreamer' or S == 'eraser' or S == 'dream' or S == 'erase':
        return True
    if S.endswith('dreamer'):
        return f(S[:-7])
    if S.endswith('eraser'):
        return f(S[:-6])
    if S.endswith('dream') or S.endswith('erase'):
        return f(S[:-5])
    return False

def main():
    S = input()
    if f(S):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
