from unittest import TestCase

from test.strategy_performance_service import StrategyPerformanceService

service = StrategyPerformanceService()


class TestStrategyPerformance(TestCase):

    def test_the_time_taken_to_process_1000_items_by_brute_force_must_be_greater_than_divide_and_conquer(self):
        # given
        service.clear()
        total_items = 1000

        # when
        service.take_measurement_of(total_items)

        # then
        service.plot_result()
        self.assertTrue(
            service.brute_force_total_time() > service.divide_and_conquer_total_time())

    def test_the_time_taken_to_process_2500_items_by_brute_force_must_be_greater_than_divide_and_conquer(self):
        # given
        service.clear()
        total_items = 2500

        # when
        service.take_measurement_of(total_items)

        # then
        service.plot_result()
        self.assertTrue(
            service.brute_force_total_time() > service.divide_and_conquer_total_time())

    def test_the_time_taken_to_process_5000_items_by_brute_force_should_be_greater_than_divide_and_conquer(self):
        # given
        service.clear()
        total_items = 5000

        # when
        service.take_measurement_of(total_items)

        # then
        service.plot_result()
        self.assertTrue(
            service.brute_force_total_time() > service.divide_and_conquer_total_time())

    def test_the_time_taken_to_process_10000_items_by_brute_force_should_be_greater_than_divide_and_conquer(self):
        # given
        service.clear()
        total_items = 10000

        # when
        service.take_measurement_of(total_items)

        # then
        service.plot_result()
        self.assertTrue(
            service.brute_force_total_time() > service.divide_and_conquer_total_time())
