# -*- coding: utf-8 -*-


def ParseLog(log):

    race_data = []

    for line in log.splitlines()[1:]:
        line = line.split()
        line.remove(line[2])
        race_data.append(line)

    return race_data


def ParseCodPilotos(log):

    cod_pilotos = []

    for line in log.splitlines()[1:]:
        line = line.split()
        cod_pilotos.append(line[1])

    cod_pilotos = list(set(cod_pilotos))

    return cod_pilotos
