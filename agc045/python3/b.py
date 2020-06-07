def main():
    S = input()
    cnt_zero = S.count('0')
    cnt_one  = S.count('1')
    cnt_diff = abs(cnt_one - cnt_zero)
    if cnt_diff > cnt_qstn:
        cnt_diff - cnt_qstn
    else:
        if cnt_diff % 2 == 1:
            print(1)
        else:
            print(0)
    
    cnt_qstn = S.count('?')
    print(cnt_zero, cnt_one, cnt_qstn)


if __name__ == '__main__':
    main()

