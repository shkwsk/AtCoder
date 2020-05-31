import itertools

def is_prime(num, prime_list):
    return all(num % prime != 0 for prime in prime_list)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    N = int(input())
    divisors = make_divisors(N)[1:]
    cnt = 0
    while len(divisors) != 0:
        d = divisors.pop(0)
        if not is_prime(d, divisors):
            continue
        e = 1
        # print(d,e)
        # print('===================')
        while N%d**e == 0:
            # print(d,N,e,cnt)
            N = N/(d**e)
            e += 1
            cnt += 1
        #     print(d,N,e,cnt)
        # print('===================')
    print(cnt)

if __name__ == '__main__':
    main()
