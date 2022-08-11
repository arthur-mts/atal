from sys import argv
from timeit import default_timer as timer

mem = dict()


def fib(n):
    if n == 1 or n == 2:
        return 1
    if mem.get(n) is not None:
        return mem.get(n)
    mem[n - 1] = fib(n - 1)
    mem[n - 2] = fib(n - 2)
    return mem[n - 1] + mem[n - 2]


if __name__ == '__main__':
    i = int(input())
    mem = dict()
    start = timer()
    result = fib(i)
    end = timer()
    print("{}: {} : {:.7f}s".format(i, result, (end - start)))
