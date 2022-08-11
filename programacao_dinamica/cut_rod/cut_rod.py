def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
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
