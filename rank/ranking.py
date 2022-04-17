from rank.rank import Rank


class Ranking:

    def __init__(self):
        self.ranks = dict()

    def add(self, rank):
        self.ranks[rank.player_name] = rank

    def exist(self, player_name):
        return player_name in self.ranks

    def increase_wins_of(self, player_name):
        rank = self.ranks.get(player_name)
        rank.defeat_a_rival()

    def defeated_players_of(self, player_name):
        return self.ranks[player_name].defeated_rivals

    def get_rank(self, index):
        for rank in self.ranks.items():
            if rank[1].position == index:
                return rank[1]
