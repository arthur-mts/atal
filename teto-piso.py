def teto_piso(n, a, k):
    def piso(a, k, start, end):
        idx = (end + start) // 2
        if idx == 0:
            return a[idx] if a[idx] <= k else -1
        elif a[idx] >= k:



    def teto_piso_aux(a, k, start, end):
        idx = (end + start) // 2

        if idx == 0:
            print(f"teto = {a[idx]}, piso = {a[idx]}")
            teto = a[idx] if a[idx] >= k else -1
            piso = a[idx] if a[idx] <= k else -1
            return a[idx], a[idx]

        if a[idx] > k:
            if a[idx]
            else:
            # Se o numero na posição i é maior que nosso K, temos certeza que o
            return teto_piso_aux(a, k, start, idx)


if __name__ == '__main__':
