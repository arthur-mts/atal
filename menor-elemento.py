def less_missing(n, a):
    def less_missing_aux(a, start, end):
        idx = (end + start) // 2
        if a[idx] == idx:
            return less_missing_aux(a, idx, end)
        elif a[idx] > idx:
            if idx == 0:
                return 0
            elif a[idx - 1] == idx - 1:
                return idx
            else:
                return less_missing_aux(a, start, idx)

    return less_missing_aux(a, 0, n)


if __name__ == '__main__':
    print("Casos teste disponibilizados")
    a = [0, 1, 2, 6, 9, 11, 15]
    print(a)
    print(less_missing(7, a))
    a = [1, 2, 3, 4, 6, 9, 11, 15]
    print(a)
    print(less_missing(8, a))
    a = [0, 1, 2, 3, 4, 5, 6, 8]
    print(a)
    print(less_missing(8, a))
