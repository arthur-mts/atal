def mochila_recursivo(s, n, w):
    if n == 0 or w == 0:
        return 0

    if s[n]["w"] > w:
        return mochila_recursivo(s, n - 1, w)
    else:
        return max(
            s[n]["v"] + mochila_recursivo(s, n - 1, (w - s[n]["w"])),
            mochila_recursivo(s, n - 1, w)
        )


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

    print(mochila_recursivo(s, n, w))
