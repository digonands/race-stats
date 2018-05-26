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


def RaceDataByPiloto(race_data, cod_pilotos):

    piloto_race_data = []

    for cod_piloto in cod_pilotos:
        piloto_race_data.append([x for x in race_data if x[1] == cod_piloto])

    return piloto_race_data


def GetLastLapData(piloto_race_data):

    last_lap_results = []

    for p in piloto_race_data:
        last_lap = p[-1]
        last_lap_results.append(last_lap)

    last_lap_results.sort()

    return last_lap_results
