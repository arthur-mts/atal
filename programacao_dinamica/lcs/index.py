import random
import time

from lcs_memorizado import lcs_memorizado
from lcs_recursivo import lcs_recursivo
from lcs_dinamico import lcs_dinamico


def random_string(l):
    return ''.join(random.choice('ACGT') for _ in range(l))

def main():
    l1 = 20
    l2 = 15
    s1 = random_string(l1)
    s2 = random_string(l2)

    start = time.time()
    print(f'Função recursiva: {lcs_recursivo(s1, s2, l1, l2)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f'Função memorizada: {lcs_memorizado(s1, s2, l1, l2)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f'Função dinâmica: {lcs_dinamico(s1, s2, l1, l2)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")


if __name__ == '__main__':
    main()