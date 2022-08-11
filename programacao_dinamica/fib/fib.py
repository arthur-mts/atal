from sys import argv
from timeit import default_timer as timer


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    i = int(input())
    start = timer()
    result = fib(i)
    end = timer()
    print("{}: {} : {:.7f}s".format(i, result, (end - start)))
