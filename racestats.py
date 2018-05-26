# -*- coding: utf-8 -*-
import datetime as dt


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


def CalculatePilotoTotalTime(race_data, cod_piloto):

    time_list = [dt.datetime.strptime(x[-2], '%M:%S.%f')
                 for x in race_data if x[1] == cod_piloto]
    minutes_sum, seconds_sum, microseconds_sum = (0, 0, 0)

    for time in time_list:
        minutes_sum += time.minute
        seconds_sum += time.second
        microseconds_sum += time.microsecond

    total_time = dt.timedelta(
        minutes=minutes_sum,
        seconds=seconds_sum,
        microseconds=microseconds_sum
    )

    return str(total_time)[:-3]


def ShowRaceResults(race_data, last_lap_data):

    header = "Posição\t\tCódigo Piloto\tNome Piloto\tVoltas Completadas\tTempo Total"
    print(header)
    posicao = 1
    results = last_lap_data

    for r in results:
        total_time = CalculatePilotoTotalTime(race_data, r[1])
        print("{0}°\t\t{1:15} {2:15} {3:23} {4}".format(
            posicao, r[1], r[2], r[3], total_time))
        posicao += 1

