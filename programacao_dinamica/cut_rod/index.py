import time

from random import randint

from cut_rod_memoizado import cut_rod_memoizado

from cut_rod import cut_rod

from cut_rod_pd import cut_rod_pd

if __name__ == '__main__':
    j = 20
    p = dict()
    for i in range(1, j + 1):
        p[i] = randint(i * 10 + 1, (i + 1) * 10)

    n = 20

    start = time.time()
    print(f"Corte de hastes recursivo: {cut_rod(p, n)}")
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f"Corte de hastes memorizado: {cut_rod_memoizado(p, n)}")
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f"Corte de hastes dinamico: {cut_rod_pd(p, n)}")
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")
