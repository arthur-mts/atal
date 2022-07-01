def teto_piso(n, a, k):
    # encontrar o teto e partir dele o piso
    def teto_piso_aux(a, k, start, end):
        idx = (end + start) // 2

        ## Se idx for 0, ele é o piso
        if end - start <= 1:
            if a[idx] > k:
                piso = -1
            else:
                piso = a[idx]

            if piso == k:
                teto = k
            elif end == n:
                teto = -1
            elif piso == -1:
                teto = a[idx]
            else:
                teto = a[idx + 1]

            return teto, piso

        if a[idx] > k:
            return teto_piso_aux(a, k, start, idx)
        else:
            return teto_piso_aux(a, k, idx, end)

    return teto_piso_aux(a, k, 0, n)


if __name__ == '__main__':
    a = [1, 4, 6, 8, 9]
    # teto, piso = teto_piso(5, a, 9)
    for i in range(11):
        teto, piso = teto_piso(5, a, i)
        print(f"k = {i} __>teto={teto}, piso={piso}")
