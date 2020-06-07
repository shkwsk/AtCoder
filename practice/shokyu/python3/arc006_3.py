def main():
    N = int(input())
    W = []
    for _ in range(N):
        W.append(int(input()))
    mount = [W.pop(0)]
    tmp_w = 0
    while len(W) != 0:
        w = W.pop(0)
        candidate = []
        for m in mount:
            if m >= w:
                candidate.append(m)
        candidate = [m for m in mount if m >= w]
        if len(candidate) == 0:
            mount.append(w)
        else:
            mount[mount.index(min(candidate))] = w
        # print(w,W,mount)
    print(len(mount))

if __name__ == '__main__':
    main()
