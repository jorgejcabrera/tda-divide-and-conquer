class Ranking:

    def __init__(self):
        self.ranks = []

    def add(self, rank):
        self.ranks.append(rank)

    def get_rank(self, index):
        return self.ranks[index - 1]
