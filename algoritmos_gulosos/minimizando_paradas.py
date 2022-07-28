def calcular_paradas(distancia, km_tanque, paradas: list):
    paradas_escolhidas = []

    km_possiveis = km_tanque

    i = 0
    while len(paradas) >= i:
        if i == 0:
            m = paradas[i]
        else:
            if i == len(paradas):
                m = distancia - paradas[i - 1]
            else:
                m = paradas[i] - paradas[i - 1] if i < len(paradas) - 1 else distancia - paradas[i]

        if m > km_possiveis:
            paradas_escolhidas.append(paradas[i - 1])
            km_possiveis = km_tanque

        km_possiveis = km_possiveis - m
        i += 1

    return paradas_escolhidas


if __name__ == '__main__':
    # distancia = int(input())
    # km_por_tanque = int(input())
    # n = int(input())
    #
    # paradas_str = input().split(' ')
    # paradas = [int(paradas_str[i]) for i in range(n)]

    distancia = 900
    km_por_tanque = 400
    n = 4
    paradas = [200, 375, 550, 750]

    print(calcular_paradas(distancia, km_por_tanque, paradas))
