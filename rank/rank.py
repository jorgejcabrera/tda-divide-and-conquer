class Rank:

    def __init__(self, player_name, position, improvement):
        self.player_name = player_name
        self.position = position
        self.improvement = improvement

    def __repr__(self) -> str:
        return f'[name:{self.player_name},position:{self.position},improvement:{self.improvement}]'

    def improve(self):
        self.improvement += 1

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.player_name == other.player_name and
                self.position == other.position and
                self.improvement == other.improvement
        )
