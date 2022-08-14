from programacao_dinamica import utils


def mochila_memorizado(s, n, w):
    memory = utils.build_memory(n, w)

    def mochila_memorizado_aux(s, n, w):
        if n == 0 or w == 0:
            return 0
        if memory[n][w] != utils.EMPTY_CELL:
            return memory[n][w]
        if s[n]['w'] > w:
            memory[n][w] = mochila_memorizado_aux(s, n - 1, w)
        else:
            decreased_weight = w - s[n]['w']
            memory[n][w] = max(
                s[n]['v'] + mochila_memorizado_aux(s, n - 1, decreased_weight),
                mochila_memorizado_aux(s, n - 1, w)
            )
        return memory[n][w]

    return mochila_memorizado_aux(s, n, w)


if __name__ == '__main__':
    s = {
        1: {
            "w": 6,
            "v": 30
        }, 2: {
            "w": 3,
            "v": 14
        }, 3: {
            "w": 4,
            "v": 16
        },
        4: {
            "w": 2,
            "v": 9
        }
    }

    w = 10

    n = len(s.keys())

    print(mochila_memorizado(s, n, w))
