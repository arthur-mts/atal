def calcular_paradas(distancia, km_tanque, paradas: list):
    def eh_solucao(paradas_escolhidas):
        return paradas_escolhidas[-1] == paradas[-1]


    paradas_escolhidas = []

    while len(paradas) > 0 and eh_solucao(paradas_escolhidas):
        parada_cor =
    return 0



if __name__ == '__main__':
    distancia = int(input())
    km_por_tanque = int(input())
    n = int(input())

    paradas_str = input().split(' ')
    paradas = [int(paradas_str[i]) for i in range(n)]

