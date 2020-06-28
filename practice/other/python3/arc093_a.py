def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    max_val = 0
    A = [0] + A + [0]
    for i in range(len(A)):
        max_val += abs(A[i]-A[i-1])
    for i in range(1,len(A)-1):
        print(max_val + abs(A[i-1]-A[i+1]) - abs(A[i-1]-A[i]) - abs(A[i]-A[i+1]))

if __name__ == '__main__':
    main()
