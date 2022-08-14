EMPTY_CELL = '-'


def build_memory(n, w):
    memory = list()
    for i in range(n + 1):
        memory.append(list())
        for j in range(w + 1):
            if i == 0 or j == 0:
                memory[i].append(0)
            else:
                memory[i].append(EMPTY_CELL)
    return memory
