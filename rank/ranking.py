from rank.rank import Rank


class Ranking:

    def __init__(self):
        self.ranks = dict()

    def add(self, rank):
        self.ranks[rank.player_name] = rank

    # TODO refactor esta raro esto, debería chequearse si existe por fuera y luego agregar
    def add_if_not_exist(self, player_name, position):
        if player_name not in self.ranks:
            self.ranks[player_name] = Rank(
                player_name=player_name,
                position=position,
                defeated_rivals=0
            )

    # TODO refactor solo debería incrementar la cantidad de rivales vencidos
    def defeat_a_rival(self, player_name, position):
        if player_name in self.ranks:
            rank = self.ranks.get(player_name)
            rank.defeat_a_rival()
        else:
            self.ranks[player_name] = Rank(
                player_name=player_name,
                position=position,
                defeated_rivals=1
            )

    def defeated_players_of(self, player_name):
        return self.ranks[player_name].defeated_rivals

    def get_rank(self, index):
        for rank in self.ranks.items():
            if rank[1].position == index:
                return rank[1]
