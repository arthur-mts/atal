def cut_rod_pd(p, n):
    memory = {}
    memory[0] = 0
    memory[1] = p[1]
    for i in range(2, n + 1):
        best_choice = p[i]
        for j in range(1, i // 2 + 1):
            # print(f"Haste tamanho {i}, combinação {i - j}-{j}")
            choice = memory[i - j] + memory[j]
            if choice > best_choice:
                best_choice = choice
        memory[i] = best_choice
        # print("\n")
    return memory[n]
    # 1: 1 + 0
    # 2: 1 + 1; 2 + 0
    # 3: 1 + 2; 3 + 0
    # 4: 1 + 3; 2 + 2; 4 + 0
    # 5: 1 + 4; 2 + 3; 5 + 0
    # 6: 1 + 5; 2 + 4; 3 + 3; 6 + 0
    # 7: 1 + 6; 2 + 5; 3 + 4; 7 + 0
    # 8: 1 + 7; 2 + 6; 3 + 5; 4 + 4; 8 + 0


if __name__ == '__main__':
    p = {
        1: 1,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 20,
        9: 24,
        10: 30
    }
    print(cut_rod_pd(p, 5))
