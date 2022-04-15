from player.player_record import PlayerRecord


def instance_one():
    return [
        PlayerRecord(name="A", previous_rank=3),
        PlayerRecord(name="B", previous_rank=4),
        PlayerRecord(name="C", previous_rank=2),
        PlayerRecord(name="D", previous_rank=8),
        PlayerRecord(name="E", previous_rank=6),
        PlayerRecord(name="F", previous_rank=5),
    ]
