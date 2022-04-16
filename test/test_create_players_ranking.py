from unittest import TestCase

from create_players_ranking import CreatePlayersRanking
from rank.rank import Rank
from test.player_record_factory import instance_one, instance_two, instance_three, instance_four, instance_five


class TestCreatePlayersRanking(TestCase):

    # A,3|B,4|C,2|D,8|E,6|F,5
    def test_using_brute_force_with_instance_one(self):
        # given
        players_record = instance_one()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_one_was_created(ranking)

    # A,3|B,4|C,2|D,8|E,6|F,5
    def test_using_divide_and_conquer_with_instance_one(self):
        # given
        players_record = instance_one()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_divide_and_conquer(players_record)

        # then
        self.then_the_expected_ranking_for_instance_one_was_created(ranking)

    # A,5|B,1|C,4|D,3|E,2|F,8|G,6|H,7
    def test_using_brute_force_with_instance_two(self):
        # given
        players_record = instance_two()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_two_was_created(ranking)

    # TODO fix this test
    # A,5|B,1|C,4|D,3|E,2|F,8|G,6|H,7
    def test_using_divide_and_conquer_with_instance_two(self):
        # given
        players_record = instance_two()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_divide_and_conquer(players_record)

        # then
        self.then_the_expected_ranking_for_instance_two_was_created(ranking)

    # A,2|B,1|C,4|D,3
    def test_using_brute_force_strategy_with_instance_three(self):
        # given
        players_record = instance_three()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_three_was_created(ranking)

    # A,2|B,1|C,4|D,3
    def test_using_divide_and_conquer_strategy_with_instance_three(self):
        # given
        players_record = instance_three()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_three_was_created(ranking)

    # A,4|B,1|C,2|D,3
    def test_using_divide_and_conquer_strategy_with_instance_four(self):
        # given
        players_record = instance_four()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_four_was_created(ranking)

    # A,4|B,1|C,2|D,3
    def test_using_brute_force_strategy_with_instance_four(self):
        # given
        players_record = instance_four()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_four_was_created(ranking)

    # A,3|B,4|C,2
    def test_using_brute_force_strategy_with_instance_five(self):
        # given
        players_record = instance_five()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.then_the_expected_ranking_for_instance_five_was_created(ranking)

    # A,3|B,4|C,2
    def test_using_divide_and_conquer_strategy_with_instance_five(self):
        # given
        players_record = instance_five()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_divide_and_conquer(players_record)

        # then
        self.then_the_expected_ranking_for_instance_five_was_created(ranking)

    def then_the_expected_ranking_for_instance_two_was_created(self, ranking):
        self.assertTrue(Rank(player_name="A", position=1, improvement=4) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", position=2, improvement=0) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", position=3, improvement=1) == ranking.get_rank(3))
        self.assertTrue(Rank(player_name="D", position=4, improvement=0) == ranking.get_rank(4))
        self.assertTrue(Rank(player_name="E", position=5, improvement=0) == ranking.get_rank(5))
        self.assertTrue(Rank(player_name="F", position=6, improvement=2) == ranking.get_rank(6))
        self.assertTrue(Rank(player_name="G", position=7, improvement=0) == ranking.get_rank(7))
        self.assertTrue(Rank(player_name="H", position=8, improvement=0) == ranking.get_rank(8))

    def then_the_expected_ranking_for_instance_one_was_created(self, ranking):
        self.assertTrue(Rank(player_name="A", position=1, improvement=1) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", position=2, improvement=1) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", position=3, improvement=0) == ranking.get_rank(3))
        self.assertTrue(Rank(player_name="D", position=4, improvement=2) == ranking.get_rank(4))
        self.assertTrue(Rank(player_name="E", position=5, improvement=1) == ranking.get_rank(5))
        self.assertTrue(Rank(player_name="F", position=6, improvement=0) == ranking.get_rank(6))

    def then_the_expected_ranking_for_instance_three_was_created(self, ranking):
        self.assertTrue(Rank(player_name="A", position=1, improvement=1) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", position=2, improvement=0) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", position=3, improvement=1) == ranking.get_rank(3))
        self.assertTrue(Rank(player_name="D", position=4, improvement=0) == ranking.get_rank(4))

    def then_the_expected_ranking_for_instance_four_was_created(self, ranking):
        self.assertTrue(Rank(player_name="A", position=1, improvement=3) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", position=2, improvement=0) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", position=3, improvement=0) == ranking.get_rank(3))
        self.assertTrue(Rank(player_name="D", position=4, improvement=0) == ranking.get_rank(4))

    def then_the_expected_ranking_for_instance_five_was_created(self, ranking):
        self.assertTrue(Rank(player_name="A", position=1, improvement=1) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", position=2, improvement=1) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", position=3, improvement=0) == ranking.get_rank(3))
