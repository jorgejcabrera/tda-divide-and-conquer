from rank.rank import Rank
from rank.ranking import Ranking


def has_improve_his_rank(index, player):
    return index < player.previous_rank - 1


def amount_of_defeated_players(index, players_record, player_record):
    next_index = index + 1
    improvement = 0
    while next_index <= player_record.previous_rank - 1 and len(players_record) > next_index:
        other_player_record = players_record[next_index]
        if other_player_record.previous_rank < player_record.previous_rank:
            improvement += 1
        next_index += 1
    return improvement


class CreatePlayersRanking:

    def __init__(self):
        return

    # #
    # complejidad temporal de O(n^2)
    # #
    def execute_by_brute_force(self, players_record):
        rankings = Ranking()
        for index, player_record in enumerate(players_record):
            rank = Rank(player_name=player_record.name, rank=index + 1, improvement=0)
            if has_improve_his_rank(index, player_record):
                improvement = amount_of_defeated_players(index, players_record, player_record)
                rank.improvement = improvement
            rankings.add(rank)
        return rankings
