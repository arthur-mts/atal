def freq_duplicadas(a, n):
    def freq_duplicadas_aux(a, ini, fim):
        meio = (ini + fim) // 2
        if a[ini] == a[meio]:
            if (meio + 1 < n and a[meio + 1] != a[ini]) or (meio + 1 == n):
                print(f"{a[ini]} ocorre {(meio - ini) + 1} vezes")
                freq_duplicadas_aux(a, meio + 1, fim)
        else:
            if ini > fim:
                return
            freq_duplicadas_aux(a, ini, meio)
            freq_duplicadas_aux(a, meio + 1, fim)

    freq_duplicadas_aux(a, 0, n)


if __name__ == '__main__':
    freq_duplicadas([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9], 11)
