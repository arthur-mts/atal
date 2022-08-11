from sys import maxsize as inf


def cut_rod_memoizado(p, n):
    r = {0: 0}
    for i in range(1, n + 1):
        r[i] = -inf
    out = cut_rod_memoizado_aux(p, n, r)
    return out


def cut_rod_memoizado_aux(p, n, memory):
    if memory[n] >= 0:
        return memory[n]
    else:
        q = 0
        for i in range(1, n + 1):
            previous_result = cut_rod_memoizado_aux(p, n - i, memory)
            q = max(q, p[i] + previous_result)
        memory[n] = q
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
        8: 20,
        9: 24,
        10: 30
    }

    print(cut_rod_memoizado(p, 5))
