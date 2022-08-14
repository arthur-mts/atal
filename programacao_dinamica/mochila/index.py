import time
from random import randint
from mochila_dinamico import mochila_dinamico

from mochila_memorizado import mochila_memorizado

from mochila_recursivo import mochila_recursivo

def main():
    s = dict()

    w = 30

    n = 30

    for i in range(n + 1):
        s[i] = {
            'w': randint(1, 8),
            'v': randint(11, 16)
        }

    start = time.time()
    print(f'Função recursiva: {mochila_recursivo(s, n, w)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f'Função memorizada: {mochila_memorizado(s, n, w)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")

    start = time.time()
    print(f'Função dinâmica: {mochila_dinamico(s, n, w)}')
    end = time.time()
    print("Tempo de execução: " + "%.8f" % (end - start) + "\n")


if __name__ == '__main__':
    main()