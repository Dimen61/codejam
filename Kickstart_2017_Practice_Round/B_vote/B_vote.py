T = int(input())

for t in range(T):
    n, m = [int(x) for x in input().split()]
    print('Case #{0}: {1}'.format(t+1, (n-m) / (n+m)))
