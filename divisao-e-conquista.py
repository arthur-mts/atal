## Questão 1

## Resolução O(n/2)
def mean(size, a, b):
    count = 0
    idx_ma = 0
    idx_mb = 0
    aux = []
    while count <= size:
        if a[idx_ma] <= b[idx_mb]:
            aux.append(a[idx_ma])
            idx_ma += 1
        else:
            aux.append(b[idx_mb])
            idx_mb += 1
        count += 1

    return (aux[size] + aux[size - 1]) / 2


def meanlogn(size, a, b, centerA=None, centerB=None):
    if centerA is None and centerB is None:
        return meanlogn(size, a, b, size // 2, size // 2)

    elif a[centerA] == b[centerB]:
        return a[centerA]
    # Analisa a parte maior de A e a menor de B
    elif a[centerA] < b[centerB]:
        return meanlogn(size, a, b, (size + centerA) // 2, centerB // 2)


if __name__ == '__main__':
    print(mean(5, [2, 3, 6, 7, 9], [1, 2, 6, 10, 11]))
