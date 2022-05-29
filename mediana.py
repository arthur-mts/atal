import statistics
import numpy as np


## Questão 1
## TODO: Calcular complexidade
def median_imp(size, a, b):
    def median_aux(ini_a, end_a, ini_b, end_b, a, b):
        ma = (ini_a + end_a) // 2
        mb = (ini_b + end_b) // 2

        if a[ma] == b[mb]:
            return (a[ma] + b[mb]) / 2
        elif end_a - ini_a <= 1 and end_b - ini_b <= 1:
            if a[ma] > b[mb]:
                return (a[end_a] + b[ini_b]) / 2
            else:
                return (a[ini_a] + b[end_b]) / 2
        elif a[ma] <= b[mb]:
            return median_aux(ma, end_a, ini_b, mb, a, b)
        else:
            return median_aux(ini_a, ma, mb, end_b, a, b)

    return median_aux(0, size, 0, size, a, b)


if __name__ == '__main__':
    print("Casos testes disponibilizados")
    SIZE = 5
    a, b = [2, 3, 6, 7, 9], [1, 2, 6, 10, 11]
    imp = median_imp(SIZE, a, b)
    target = statistics.median(a + b)
    print(a, b)
    assert imp == target
    print(imp, target)
    a, b = [0, 1, 2, 4, 5], [7, 9, 10, 12, 13]
    imp = median_imp(SIZE, a, b)
    target = statistics.median(a + b)
    print(a, b)
    assert imp == target
    print(imp, target)

    print("Casos testes aleatorios")
    SIZE = 10
    for i in range(10):
        a = np.sort(np.random.randint(20, size=SIZE))
        b = np.sort(np.random.randint(20, size=SIZE))
        print(a, b)
        imp = median_imp(SIZE, a, b)
        target = statistics.median(a + b)
        assert imp == target, f"Resultado {imp}; Resultado esperado {target}"
        print(imp, target)

