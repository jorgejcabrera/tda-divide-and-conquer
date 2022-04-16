class PlayerRecord:

    def __repr__(self) -> str:
        return f'[name:{self.name},previous_position:{self.previous_position}]'

    def __init__(self, name, previous_position):
        self.name = name
        self.previous_position = previous_position
