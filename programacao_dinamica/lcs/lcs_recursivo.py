def lcs_recursivo(s1, s2, l1, l2):
    if l1 == 0 or l2 == 0:
        return 0
    if s1[l1 - 1] == s2[l2 - 1]:
        return 1 + lcs_recursivo(s1, s2, l1 - 1, l2 - 1)
    else:
        return max(
            lcs_recursivo(s1, s2, l1, l2 - 1),
            lcs_recursivo(s1, s2, l1 - 1, l2)
        )


def main():
    print(lcs_recursivo("abcbdab", "bdcaba", 7, 6))


if __name__ == '__main__':
    main()
