class Rank:

    def __init__(self, player_name, position, defeated_rivals):
        self.player_name = player_name
        self.position = position
        # TODO revisar el nombre de la variable
        self.defeated_rivals = defeated_rivals

    def __repr__(self) -> str:
        return f'[name:{self.player_name},position:{self.position},defeated_players:{self.defeated_rivals}]\n'

    def defeat_a_rival(self):
        self.defeated_rivals += 1

    def increase_wins_by(self, wins):
        self.defeated_rivals += wins

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.player_name == other.player_name and
                self.position == other.position and
                self.defeated_rivals == other.defeated_rivals
        )
