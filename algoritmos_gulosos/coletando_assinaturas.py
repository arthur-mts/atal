INICIO = 0
FIM = 1


def coletando_assinaturas(intervalos: list):
    i = 0
    intervalo_cur = None
    intervalos_visita = []
    while i < len(intervalos):
        if intervalo_cur is None:
            intervalo_cur = intervalos[i]

        elif i < len(intervalos):
            if intervalos[i][INICIO] <= intervalo_cur[FIM]:
                intervalo_cur = (intervalos[i][INICIO], intervalo_cur[FIM])
            else:
                intervalos_visita.append(intervalo_cur)
                intervalo_cur = (intervalos[i - 1][FIM], intervalos[i][FIM])
        i += 1
    intervalos_visita.append(intervalo_cur)
    return intervalos_visita


if __name__ == '__main__':
    l = [(1, 3), (2, 5), (3, 6)]
    # l = [(1, 3), (2, 5), (4, 7)]
    print(coletando_assinaturas(l))
