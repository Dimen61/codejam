import sys

def main():
    T = int(input())
    for t in range(T):
        L, R = list(map(int, input().split()))
        M = min(L, R)

        ans = (M + 1) * M // 2

        print('Case #{0}: {1}'.format(t+1, ans))

if __name__ == '__main__':
    main()