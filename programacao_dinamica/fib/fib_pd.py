from sys import argv
from timeit import default_timer as timer


def fib(n):
    mem = dict()
    mem[1] = 1
    mem[2] = 1
    for i in range(3, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[n]


if __name__ == '__main__':
    i = int(input())
    start = timer()
    result = fib(i)
    end = timer()
    print("{}: {} : {:.7f}s".format(i, result, (end - start)))
