from collections import defaultdict
import string

def main():
    S = list(input())
    T = list(input())
    accept = False
    for i in reversed(range(len(S)-len(T)+1)):
        match = True
        for j,s in enumerate(S[i:i+len(T)]):
            if s != T[j] and s != '?':
                match = False
                break
        if match:
            S[i:i+len(T)] = T
            accept = True
            break
    if accept:
        print(''.join(S).replace('?','a'))
    else:
        print('UNRESTORABLE')


if __name__ == '__main__':
    main()
