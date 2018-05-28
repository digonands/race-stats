#!/usr/bin/env python
# -*- coding: utf-8 -*-
from racestats import (
    ParseLog,
    ParseCodPilotos,
    RaceDataByPiloto,
    GetLastLapData,
    CalculatePilotoTotalTime,
    ShowRaceResults
)
import unittest


class RaceStatsTest(unittest.TestCase):

    def setUp(self):
        """
        Setup test data
        """
        with open('race.log') as file:
            self.read_data = file.read()
        
        self.parsed_log = ParseLog(self.read_data)
        self.cod_pilotos = ParseCodPilotos(self.read_data)
        self.race_data_by_piloto = RaceDataByPiloto(
            cod_pilotos=self.cod_pilotos, race_data=self.parsed_log
        )
        self.last_lap_data = GetLastLapData(self.race_data_by_piloto)
        self.piloto_002_total_time = CalculatePilotoTotalTime(
            race_data=self.parsed_log, cod_piloto='002'
        )

    def test_parse_log(self):
        # Remove the heading line from the log
        self.assertIn('Hora', self.read_data.splitlines()[0])
        self.assertNotIn('Hora', self.parsed_log[0])
        # Convert log into a list of lines
        self.assertEqual(len(self.parsed_log), len(self.read_data.splitlines())-1)
        # Split the line with column values. It must have 6 columns
        self.assertEqual(len(self.parsed_log[0]), 6)

    def test_parse_cod_pilotos(self):
        # Get the drivers from the race. It must have 6 drivers
        self.assertEqual(self.cod_pilotos, ['002', '011', '015', '023', '033', '038'])
        self.assertEqual(len(self.cod_pilotos), 6)

    def test_race_data_by_piloto(self):
        # Group the race data by each driver
        self.assertEqual(self.race_data_by_piloto[0][0][1], '002')
        self.assertEqual(self.race_data_by_piloto[0][1][1], '002')
        self.assertEqual(self.race_data_by_piloto[2][0][1], '015')
        self.assertEqual(self.race_data_by_piloto[2][1][1], '015')
        # Check the 6 columns
        self.assertEqual(len(self.race_data_by_piloto[2][1]), 6)
        # Check the 6 drivers
        self.assertEqual(len(self.race_data_by_piloto), 6)

    def test_get_last_lap_data(self):
        # Get the last item from the list with race data grouped by driver
        for piloto_data in self.race_data_by_piloto:
            self.assertIn(piloto_data[-1], self.last_lap_data)
        self.assertEqual(len(self.last_lap_data), 6)

    def test_piloto_total_time(self):
        # Calculate the total time for the 002 driver
        # It should match with the sum of the time of each lap
        # '1:04.108' + '1:03.982' + '1:03.987' + '1:03.076' = '4:15.153'
        total_time_to_match = '4:15.153'
        self.assertEqual(self.piloto_002_total_time, total_time_to_match)

        
if __name__ == '__main__':
    unittest.main()