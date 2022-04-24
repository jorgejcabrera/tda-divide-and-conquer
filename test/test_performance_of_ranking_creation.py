from unittest import TestCase

from create_ranking import CreatePlayersRanking
from test.performance_result import PerformanceResult
from test.player_record_factory import with_size
import matplotlib.pyplot as plt

import time


def current_milli_time():
    return round(time.time() * 1000)


def sum(arr):
    total_sum = 0
    for i in range(0, len(arr)):
        total_sum = total_sum + arr[i]
    return total_sum


use_case = CreatePlayersRanking()


def total_time_by_brute_force(players_record):
    brute_force_start_time = current_milli_time()
    use_case.execute_by_brute_force(players_record)
    brute_force_total_time = current_milli_time() - brute_force_start_time
    return brute_force_total_time


def total_time_by_divide_and_conquer(players_record):
    divide_and_conquer_start_time = current_milli_time()
    use_case.execute_by_divide_and_conquer(players_record)
    divide_and_conquer_total_time = current_milli_time() - divide_and_conquer_start_time
    return divide_and_conquer_total_time


def plot_result(performance_result):
    plt.plot(performance_result.x, performance_result.total_time_by_brute_force, label='brute_force')
    plt.plot(performance_result.x, performance_result.total_time_by_divide_and_conquer, label='divide_and_conquer')
    plt.legend(loc='upper center')

    # naming the x axis
    plt.xlabel('Players')

    # naming the y axis
    plt.ylabel('Total time (ms)')

    # giving a title to my graph
    plt.title('Strategy Performance')

    # function to show the plot
    plt.show()


def get_performance_result_of(total_items):
    result = PerformanceResult()
    amount_of_players = 100

    while amount_of_players <= total_items:
        players_record = with_size(amount_of_players)

        # brute force
        result.total_time_by_brute_force.append(total_time_by_brute_force(players_record))

        # divide and conquer
        result.total_time_by_divide_and_conquer.append(total_time_by_divide_and_conquer(players_record))

        result.x.append(amount_of_players)
        amount_of_players = amount_of_players + 500

    return result


class TestPerformanceOfRankingCreation(TestCase):

    def test_the_time_taken_to_process_1000_items_by_brute_force_must_be_greater_than_divide_and_conquer(self):
        # given
        total_items = 1000

        # when
        performance_result = get_performance_result_of(total_items)

        # then
        plot_result(performance_result)
        self.assertTrue(sum(performance_result.total_time_by_brute_force) > sum(
            performance_result.total_time_by_divide_and_conquer))

    def test_the_time_taken_to_process_5000_items_by_brute_force_should_be_greater_than_divide_and_conquer(self):
        # given
        total_items = 5000

        # when
        performance_result = get_performance_result_of(total_items)

        # then
        plot_result(performance_result)
        self.assertTrue(sum(performance_result.total_time_by_brute_force) > sum(
            performance_result.total_time_by_divide_and_conquer))

    def test_the_time_taken_to_process_10000_items_by_brute_force_should_be_greater_than_divide_and_conquer(self):
        # given
        total_items = 10000

        # when
        performance_result = get_performance_result_of(total_items)

        # then
        plot_result(performance_result)
        self.assertTrue(sum(performance_result.total_time_by_brute_force) > sum(
            performance_result.total_time_by_divide_and_conquer))
