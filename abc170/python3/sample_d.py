import random

A = []
N = 2*10**5
for i in range(N):
    A.append(str(random.randint(1,10**6)))
print(N)
print(' '.join(A))
