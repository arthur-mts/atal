from random import randint


def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        # a melhor divisão de hastes para 3 é:
        # cut_rod(3 - i) + p[i]
        # i = 1:
        #   cut_rod(2) + p[1] = 5 + 1 = 6
        # i = 2:
        #   cut_rod(1) + p[2] = 1 + 5 = 6
        # i = 3:
        #   cut_rod(0) + p[3] = 0 + 8 = 8
        previous_value = cut_rod(p, n - i)
        q = max(q, p[i] + previous_value)
    return q


if __name__ == '__main__':
    p = {
        1: 1,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 24,
        10: 30
    }

    print(cut_rod(p, 5))
