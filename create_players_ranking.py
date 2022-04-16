from rank.rank import Rank
from rank.ranking import Ranking


def has_improve_his_rank(index, player):
    return index < player.previous_position - 1


def amount_of_defeated_players(index, players_record, player_record):
    next_index = index + 1
    improvement = 0
    while next_index <= player_record.previous_position - 1 and len(players_record) > next_index:
        other_player_record = players_record[next_index]
        if other_player_record.previous_position < player_record.previous_position:
            improvement += 1
        next_index += 1
    return improvement


class CreatePlayersRanking:

    def __init__(self):
        self.ranking = Ranking()

    # #
    # complejidad temporal de O(n^2)
    # #
    def execute_by_brute_force(self, players_record):
        rankings = Ranking()
        for index, player_record in enumerate(players_record):
            rank = Rank(
                player_name=player_record.name,
                position=index + 1,
                improvement=0
            )
            if has_improve_his_rank(index, player_record):
                rank.improvement = amount_of_defeated_players(index, players_record, player_record)
            rankings.add(rank)
        return rankings

    def execute_by_divide_and_conquer(self, lista):
        return self.divide_and_conquer(lista, 0)

    def divide_and_conquer(self, lista, offset):
        if len(lista) > 1:
            half = len(lista) // 2
            left = lista[:half]
            right = lista[half:]

            self.divide_and_conquer(left, offset)
            self.divide_and_conquer(right, offset + half)

            i = 0
            j = 0
            k = 0

            offset = offset + half
            while i < len(left) and j < len(right):
                if left[i].previous_position < right[j].previous_position:
                    lista[k] = left[i]
                    self.ranking.add_if_not_exist(left[i].name, offset)
                    offset = offset + 1
                    i += 1
                else:
                    self.ranking.improve_player(left[i].name, offset)
                    offset += 1
                    self.ranking.add_if_not_exist(right[j].name, offset)
                    offset += 1
                    lista[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lista[k] = left[i]
                self.ranking.add_if_not_exist(left[i].name, offset)
                offset = offset + 1
                i += 1
                k += 1

            while j < len(right):
                lista[k] = right[j]
                self.ranking.add_if_not_exist(right[j].name, offset)
                offset = offset + 1
                j += 1
                k += 1

        return self.ranking
