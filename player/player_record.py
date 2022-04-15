class PlayerRecord:

    def __repr__(self) -> str:
        return f'[name:{self.name},previous_rank:{self.previous_rank}]'

    def __init__(self, name, previous_rank):
        self.name = name
        self.previous_rank = previous_rank
