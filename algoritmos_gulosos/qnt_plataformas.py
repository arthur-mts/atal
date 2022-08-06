def quantPlataformas(chegadas, saidas):
    chegadas = sorted(chegadas)
    saidas = sorted(saidas)
    plataformas = j = k = 0

    for i in range(len(chegadas)):
        if chegadas[i] < saidas[k] and chegadas[i] < saidas[j]:
            plataformas += 1
            j = k
            k = i

    return plataformas


if __name__ == '__main__':
    chegadas, saidas = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00], [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
    print(quantPlataformas(chegadas, saidas))
