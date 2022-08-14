from programacao_dinamica import utils


def lcs_dinamico(s1, s2, l1, l2):
    memory = utils.build_memory(l1, l2)

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                memory[i][j] = 1 + memory[i - 1][j - 1]
            else:
                memory[i][j] = max(
                    memory[i - 1][j],
                    memory[i][j - 1]
                )
    return memory[l1][l2]


def main():
    print(lcs_dinamico("bdcaba", "abcbdab", 6, 7))


if __name__ == '__main__':
    main()
