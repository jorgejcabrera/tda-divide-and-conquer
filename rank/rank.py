class Rank:

    def __init__(self, player_name, rank, improvement):
        self.player_name = player_name
        self.rank = rank
        self.improvement = improvement

    def __repr__(self) -> str:
        return f'[name:{self.player_name},rank:{self.rank},improvement:{self.improvement}]'

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.player_name == other.player_name and
                self.rank == other.rank and
                self.improvement == other.improvement
        )
