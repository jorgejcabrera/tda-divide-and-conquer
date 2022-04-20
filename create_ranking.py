from rank.rank import Rank
from rank.ranking import Ranking


def amount_of_defeated_players(index, players_record):
    defeated_players = 0
    player = players_record[index]
    rivals = players_record[index:]
    for rival in rivals:
        if player.previous_position > rival.previous_position:
            defeated_players += 1
    return defeated_players


class CreatePlayersRanking:

    def __init__(self):
        self.ranking = Ranking()

    def add_if_not_exist_and_return_position(self, player, position):
        if not self.ranking.exist(player.name):
            self.ranking.add(Rank(
                player_name=player.name,
                position=position,
                defeated_rivals=0)
            )
            position += 1
        return position

    # #
    # complejidad temporal de O(n^2)
    # #
    def execute_by_brute_force(self, players_record):
        rankings = Ranking()
        for index, player_record in enumerate(players_record):
            rank = Rank(
                player_name=player_record.name,
                position=index + 1,
                defeated_rivals=0
            )
            rank.defeated_rivals = amount_of_defeated_players(index, players_record)
            rankings.add(rank)
        return rankings

    # #
    # complejidad temporal de O(n/2)^2
    # #
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

            position = offset + 1
            while i < len(left) and j < len(right):
                if left[i].previous_position < right[j].previous_position:
                    lista[k] = left[i]
                    position = self.add_if_not_exist_and_return_position(left[i], position)
                    i += 1
                else:
                    # TODO move the for loop to a method with this responsabilitie
                    for player in left[i:]:
                        if self.ranking.exist(player.name):
                            self.ranking.increase_wins_by(player.name, 1)
                        else:
                            self.ranking.add(Rank(
                                player_name=player.name,
                                position=position,
                                defeated_rivals=1)
                            )
                            position += 1
                    position = self.add_if_not_exist_and_return_position(right[j], position)
                    lista[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lista[k] = left[i]
                position = self.add_if_not_exist_and_return_position(left[i], position)
                i += 1
                k += 1

            while j < len(right):
                lista[k] = right[j]
                position = self.add_if_not_exist_and_return_position(right[j], position)
                j += 1
                k += 1

        return self.ranking
