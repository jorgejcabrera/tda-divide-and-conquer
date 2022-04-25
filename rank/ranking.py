class Ranking:

    def __repr__(self) -> str:
        return self.ranks.__repr__()

    def __init__(self):
        self.ranks = dict()

    def add(self, rank):
        self.ranks[rank.player_name] = rank

    def exist(self, player_name):
        return player_name in self.ranks

    def increase_wins_by(self, player_name, wins):
        rank = self.ranks.get(player_name)
        rank.increase_wins_by(wins)

    def defeated_players_of(self, player_name):
        return self.ranks[player_name].defeated_rivals

    def get_rank(self, index):
        for rank in self.ranks.items():
            if rank[1].position == index:
                return rank[1]
