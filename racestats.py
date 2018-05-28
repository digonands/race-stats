#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt


def ParseLog(log):
    """
    Process a log file with a race data
    """
    race_data = []

    # Read the lines from log except the heading line
    # Splits each line to get a list of values
    # Cleanup the line with unwanted stuff
    for line in log.splitlines()[1:]:
        line = line.split()
        line.remove(line[2])

        race_data.append(line)

    return race_data


def ParseCodPilotos(log):
    """
    Process a log file and get a list of the drivers from the race
    """
    cod_pilotos = []

    # Get all cod_pilotos (line[1]) and append to a list
    for line in log.splitlines()[1:]:
        line = line.split()
        cod_pilotos.append(line[1])

    # Use set to get unique values then convert to a list again
    cod_pilotos = list(set(cod_pilotos))
    # Sort values from the list
    cod_pilotos.sort()

    return cod_pilotos


def RaceDataByPiloto(race_data, cod_pilotos):
    """
    Group the data from race by driver
    """
    piloto_race_data = []

    # Use cod_pilotos (x[1]) to group the race data
    for cod_piloto in cod_pilotos:
        piloto_race_data.append([x for x in race_data if x[1] == cod_piloto])

    return piloto_race_data


def GetLastLapData(piloto_race_data):
    """
    Get only the last lap data from each driver
    """
    last_lap_results = []

    for p in piloto_race_data:
        last_lap = p[-1]
        last_lap_results.append(last_lap)

    # Make the results appear in correct order
    last_lap_results.sort()

    return last_lap_results


def CalculatePilotoTotalTime(race_data, cod_piloto):
    """
    Calculate the total time for a driver
    """

    # The time comes from race_data and it is converted to datetime format
    # The time list is selected for the given driver
    time_list = [dt.datetime.strptime(x[-2], '%M:%S.%f')
                 for x in race_data if x[1] == cod_piloto]

    # The minutes, seconds and microseconds should be sum separately
    # Then the total time is calculated by the timedelta function
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

    # Format the total time delta
    total_time_format = dt.datetime.strptime(str(total_time), '%H:%M:%S.%f')
    total_time_format = total_time_format.strftime('%-M:%S.%f')[:-3]
    return total_time_format


def ShowRaceResults(race_data, last_lap_data):
    """
    Format and print the race results
    """
    header = "Posição\t\tCódigo Piloto\tNome Piloto\tVoltas Completadas\tTempo Total"
    print(header)
    posicao = 1
    results = last_lap_data

    for r in results:
        total_time = CalculatePilotoTotalTime(race_data, r[1])
        print("{0}°\t\t{1:15} {2:15} {3:23} {4}".format(
            posicao, r[1], r[2], r[3], total_time))
        posicao += 1


def main():
    """
    The main program.
    Reads the log file then show the race results
    """
    with open('race.log') as file:
        read_data = file.read()

    parsed_log = ParseLog(read_data)
    cod_pilotos = ParseCodPilotos(read_data)
    pilotos_data = RaceDataByPiloto(parsed_log, cod_pilotos)
    last_lap_data = GetLastLapData(pilotos_data)

    print("{} is the winner!\n".format(last_lap_data[0][2]))
    ShowRaceResults(parsed_log, last_lap_data)


if __name__ == "__main__":
    main()
