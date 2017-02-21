import string

def get_diff_num(name):
    # s = set()
    # for c in name:
    #     if c in string.ascii_uppercase:
    #         s.add(c)
    # return len(s)

    total = 0
    for c in string.ascii_uppercase:
        if c in name:
            total += 1
    return total

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        names = []
        for i in range(N):
            names.append(input())

        max_num = 0
        leader = None
        for name in names:
            if not leader:
                leader = name
                max_num = get_diff_num(name)
            else:
                num = get_diff_num(name)
                if num > max_num or (num == max_num and name < leader):
                    max_num = num
                    leader = name

        print('Case #{0}: {1}'.format(t+1, leader))

if __name__ == '__main__':
    main()