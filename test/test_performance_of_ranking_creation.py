from unittest import TestCase

from create_ranking import CreatePlayersRanking
from test.player_record_factory import with_size
import matplotlib.pyplot as plt

import time


def current_milli_time():
    return round(time.time() * 1000)


class TestPerformanceOfRankingCreation(TestCase):

    def test_measure_of_brute_performance_with_15000_players(self):
        # given
        players_record = with_size(10000)
        use_case = CreatePlayersRanking()
        z_divide_and_conquer = []

        # when
        amount_of_players = 100
        x = []
        y_brute_force = []
        z_divide_and_conquer = []
        while amount_of_players <= 15000:
            players_record = with_size(amount_of_players)

            brute_force_start_time = current_milli_time()
            use_case.execute_by_brute_force(players_record)
            brute_force_total_time = current_milli_time() - brute_force_start_time
            y_brute_force.append(brute_force_total_time)

            divide_and_conquer_start_time = current_milli_time()
            use_case.execute_by_divide_and_conquer(players_record)
            divide_and_conquer_total_time = current_milli_time() - divide_and_conquer_start_time
            z_divide_and_conquer.append(divide_and_conquer_total_time)

            x.append(amount_of_players)
            amount_of_players = amount_of_players + 500

        plt.plot(x, y_brute_force)
        plt.plot(x, z_divide_and_conquer)

        # naming the x axis
        plt.xlabel('Players')
        # naming the y axis
        plt.ylabel('Total time (ms)')

        # giving a title to my graph
        plt.title('Strategy Performance')

        # function to show the plot
        plt.show()

        # then
        # self.assertTrue(brute_force_total_time > divide_and_conquer_total_time)
