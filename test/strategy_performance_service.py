import time

import matplotlib.pyplot as plt

from create_ranking import CreatePlayersRanking
from test.player_record_factory import with_size


def current_milli_time():
    return round(time.time() * 1000)


def sum(arr):
    total_sum = 0
    for i in range(0, len(arr)):
        total_sum = total_sum + arr[i]
    return total_sum


class StrategyPerformanceService:

    def __init__(self):
        self.step = 500
        self.min_amount_of_players = 100
        self.use_case = CreatePlayersRanking()
        self.x = []
        self.y_brute_force_time = []
        self.y_divide_and_conquer_time = []

    def time_for_brute_force_strategy(self, players_record):
        brute_force_start_time = current_milli_time()
        self.use_case.execute_by_brute_force(players_record)
        brute_force_total_time = current_milli_time() - brute_force_start_time
        return brute_force_total_time

    def time_for_divide_and_conquer_strategy(self, players_record):
        divide_and_conquer_start_time = current_milli_time()
        self.use_case.execute_by_divide_and_conquer(players_record)
        divide_and_conquer_total_time = current_milli_time() - divide_and_conquer_start_time
        return divide_and_conquer_total_time

    def take_measurement_of(self, total_items):
        amount_of_players = self.min_amount_of_players

        while amount_of_players <= total_items:
            players_record = with_size(amount_of_players)

            # brute force
            self.y_brute_force_time.append(self.time_for_brute_force_strategy(players_record))

            # divide and conquer
            self.y_divide_and_conquer_time.append(self.time_for_divide_and_conquer_strategy(players_record))

            self.x.append(amount_of_players)

            amount_of_players = amount_of_players + self.step

    def brute_force_total_time(self):
        return sum(self.y_brute_force_time)

    def divide_and_conquer_total_time(self):
        return sum(self.y_divide_and_conquer_time)

    def plot_result(self):
        plt.plot(self.x, self.y_brute_force_time, label='brute_force')
        plt.plot(self.x, self.y_divide_and_conquer_time, label='divide_and_conquer')
        plt.legend(loc='upper center')

        # naming the x axis
        plt.xlabel('Players')

        # naming the y axis
        plt.ylabel('Total time (ms)')

        # giving a title to my graph
        plt.title('Strategy Performance')

        # function to show the plot
        plt.show()

    def clear(self):
        self.y_brute_force_time.clear()
        self.x.clear()
        self.y_divide_and_conquer_time.clear()
