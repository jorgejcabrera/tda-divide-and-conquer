from rank.rank import Rank


class Ranking:

    def __init__(self):
        self.ranks = dict()

    def add(self, rank):
        self.ranks[rank.player_name] = rank

    def exist(self, player_name):
        return player_name in self.ranks

    def add_if_not_exist(self, player_name, position):
        if player_name not in self.ranks:
            self.ranks[player_name] = Rank(
                player_name=player_name,
                position=position,
                improvement=0
            )

    def improve_player(self, player_name, position):
        if player_name in self.ranks:
            rank = self.ranks.get(player_name)
            rank.improve()
        else:
            self.ranks[player_name] = Rank(
                player_name=player_name,
                position=position,
                improvement=1
            )

    def get_improvements_of(self, player_name):
        return self.ranks[player_name].improvement

    def get_rank(self, index):
        for rank in self.ranks.items():
            if rank[1].position == index:
                return rank[1]
