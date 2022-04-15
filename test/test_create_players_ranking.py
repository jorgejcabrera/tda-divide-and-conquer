from unittest import TestCase

from create_players_ranking import CreatePlayersRanking
from rank.rank import Rank
from test.player_record_factory import instance_one


class TestCreatePlayersRanking(TestCase):

    def test_using_brute_force_with_instance_one(self):
        # given
        players_record = instance_one()
        use_case = CreatePlayersRanking()

        # when
        ranking = use_case.execute_by_brute_force(players_record)

        # then
        self.assertTrue(Rank(player_name="A", rank=1, improvement=1) == ranking.get_rank(1))
        self.assertTrue(Rank(player_name="B", rank=2, improvement=1) == ranking.get_rank(2))
        self.assertTrue(Rank(player_name="C", rank=3, improvement=0) == ranking.get_rank(3))
        self.assertTrue(Rank(player_name="D", rank=4, improvement=2) == ranking.get_rank(4))
        self.assertTrue(Rank(player_name="E", rank=5, improvement=1) == ranking.get_rank(5))
        self.assertTrue(Rank(player_name="F", rank=6, improvement=0) == ranking.get_rank(6))
