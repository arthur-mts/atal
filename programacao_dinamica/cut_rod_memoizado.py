from random import randint
from sys import maxsize as inf


def cut_rod_memoizado(p, n):
    r = {}
    r[0] = 0
    for i in range(1, n + 1):
        r[i] = -inf
    exp = {}
    out = cut_rod_memoizado_aux(p, n, r,exp)
    # for i in exp.keys():
    #     print(exp.get(i))
    print(r)
    return out


def cut_rod_memoizado_aux(p, n, memory, explain):
    if memory[n] >= 0:
        return memory[n]
    else:
        q = 0
        # 1 -- 10
        for i in range(1, n + 1):
            previous_result = cut_rod_memoizado_aux(p, n - i, memory, explain)
            q = max(q, p[i] + previous_result)
            print(f"({i}+{n - i}) previous result={previous_result};n={n};q={q}")
            explain[(i, n-i)] = f"({i}+{n - i}) previous result={previous_result};n={n};q={q}"
        print("\n")
        memory[n] = q
        return q


if __name__ == '__main__':
    tam = 8

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

    print(cut_rod_memoizado(p, tam))
