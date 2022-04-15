from player.player_record import PlayerRecord


def instance_one():
    # A,3|B,4|C,2|D,8|E,6|F,5
    return [
        PlayerRecord(name="A", previous_rank=3),
        PlayerRecord(name="B", previous_rank=4),
        PlayerRecord(name="C", previous_rank=2),
        PlayerRecord(name="D", previous_rank=8),
        PlayerRecord(name="E", previous_rank=6),
        PlayerRecord(name="F", previous_rank=5),
    ]


def instance_two():
    # A,5|B,1|C,4|D,3|E,2|F,8|G,6|H,7
    return [
        PlayerRecord(name="A", previous_rank=5),
        PlayerRecord(name="B", previous_rank=1),
        PlayerRecord(name="C", previous_rank=4),
        PlayerRecord(name="D", previous_rank=3),
        PlayerRecord(name="E", previous_rank=2),
        PlayerRecord(name="F", previous_rank=8),
        PlayerRecord(name="G", previous_rank=6),
        PlayerRecord(name="H", previous_rank=7),
    ]
