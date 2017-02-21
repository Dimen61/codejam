# def main():
#     with open('./A-small-practice.in', 'r') as fin:
#         lines = fin.read().split('\n')
#         output = ''

#         N = int(lines[0])
#         for i in range(N):
#             C = int(lines[1+3*i])
#             I = int(lines[2+3*i])
#             items = zip(list(map(int, lines[3+3*i].split())), list(range(I)))

#             for i in range(len(items)):
#                 if (C - items[i]) in items:
#                     output += 'Case #{0}: {1} {2}\n'.format(i+1, i, C-item)
#                     break

#         with open('./A-small-practice.out', 'w') as fout:
#             fout.write(output)

# if __name__ == '__main__':
#     main()


import sys

def main():
    try:
        fin = open('./A-large-practice.in', 'r')
        fout = open('./A-large-practice.out', 'w')
        sys.stdin = fin
        sys.stdout = fout

        N = int(input())        
        for i in range(N):
            C = int(input())
            I = int(input())
            prices = list(map(int, input().split()))

            items = dict(zip(prices, range(len(prices))))

            for j in range(len(prices)):
                if C - prices[j] in items:
                    print('Case #{0}: {1} {2}'.format(i+1, j+1, items[C-prices[j]]+1))
                    break


    finally:
        fin.close()
        fout.close()
















if __name__ == '__main__':
    main()