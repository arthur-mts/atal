from programacao_dinamica import utils


def lcs_memorizado(s1, s2, l1, l2):
    memory = utils.build_memory(l1, l2)

    def lcs_memorizado_aux(s1, s2, l1, l2):
        if l1 == 0 or l2 == 0:
            return 0
        if memory[l1][l2] != utils.EMPTY_CELL:
            return memory[l1][l2]
        if s1[l1 - 1] == s2[l2 - 1]:
            memory[l1][l2] = 1 + lcs_memorizado_aux(s1, s2, l1 - 1, l2 - 1)
        else:
            memory[l1][l2] = max(
                lcs_memorizado_aux(s1, s2, l1, l2 - 1),
                lcs_memorizado_aux(s1, s2, l1 - 1, l2)
            )
        return memory[l1][l2]

    return lcs_memorizado_aux(s1, s2, l1, l2)


def main():
    print(lcs_memorizado("abcbdab", "bdcaba", 7, 6))


if __name__ == '__main__':
    main()
