from programacao_dinamica import utils


def mochila_dinamico(s, n, w):
    memory = utils.build_memory(w, n)

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if s[i]['w'] > j:
                memory[j][i] = memory[j][i - 1]
            else:
                memory[j][i] = max(
                    memory[j - s[i]['w']][i - 1] + s[i]['v'],
                    memory[j][i - 1]
                )

    return memory[w][n]


if __name__ == '__main__':
    s = {
        1: {"w": 6, "v": 20},
        2: {"w": 2, "v": 15},
        3: {"w": 1, "v": 2},
        4: {"w": 4, "v": 12},
        5: {"w": 3, "v": 7}
    }
    w = 5

    n = len(s.keys())

    print(mochila_dinamico(s, n, w))
