class Rank:

    def __init__(self, player_name, position, defeated_players):
        self.player_name = player_name
        self.position = position
        self.defeated_players = defeated_players

    def __repr__(self) -> str:
        return f'[name:{self.player_name},position:{self.position},defeated_players:{self.defeated_players}]'

    def improve(self):
        self.defeated_players += 1

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.player_name == other.player_name and
                self.position == other.position and
                self.defeated_players == other.defeated_players
        )
