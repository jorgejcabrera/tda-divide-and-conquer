from player.player_record import PlayerRecord
import random


def instance_one():
    # A,3|B,4|C,2|D,8|E,6|F,5
    return [
        PlayerRecord(name="A", previous_position=3),
        PlayerRecord(name="B", previous_position=4),
        PlayerRecord(name="C", previous_position=2),
        PlayerRecord(name="D", previous_position=8),
        PlayerRecord(name="E", previous_position=6),
        PlayerRecord(name="F", previous_position=5),
    ]


def instance_two():
    # A,5|B,1|C,4|D,3|E,2|F,8|G,6|H,7
    return [
        PlayerRecord(name="A", previous_position=5),
        PlayerRecord(name="B", previous_position=1),
        PlayerRecord(name="C", previous_position=4),
        PlayerRecord(name="D", previous_position=3),
        PlayerRecord(name="E", previous_position=2),
        PlayerRecord(name="F", previous_position=8),
        PlayerRecord(name="G", previous_position=6),
        PlayerRecord(name="H", previous_position=7),
    ]


def instance_three():
    # A,2|B,1|C,4|D,3
    return [
        PlayerRecord(name="A", previous_position=2),
        PlayerRecord(name="B", previous_position=1),
        PlayerRecord(name="C", previous_position=4),
        PlayerRecord(name="D", previous_position=3)
    ]


def instance_four():
    # A,4|B,1|C,2|D,3
    return [
        PlayerRecord(name="A", previous_position=4),
        PlayerRecord(name="B", previous_position=1),
        PlayerRecord(name="C", previous_position=2),
        PlayerRecord(name="D", previous_position=3)
    ]


def instance_five():
    # A,3|B,4|C,2
    return [
        PlayerRecord(name="A", previous_position=3),
        PlayerRecord(name="B", previous_position=4),
        PlayerRecord(name="C", previous_position=2)
    ]


def instance_six():
    # A,5|B,2|C,4|D,3|E,1
    return [
        PlayerRecord(name="A", previous_position=5),
        PlayerRecord(name="B", previous_position=2),
        PlayerRecord(name="C", previous_position=4),
        PlayerRecord(name="D", previous_position=3),
        PlayerRecord(name="E", previous_position=1)
    ]


def instance_seven():
    # A,5|B,11|C,2|D,9|E,3|F,10|G,7|H,4|I,6|J,8|K,1
    return [
        PlayerRecord(name="A", previous_position=5),
        PlayerRecord(name="B", previous_position=11),
        PlayerRecord(name="C", previous_position=2),
        PlayerRecord(name="D", previous_position=9),
        PlayerRecord(name="E", previous_position=3),
        PlayerRecord(name="F", previous_position=10),
        PlayerRecord(name="G", previous_position=7),
        PlayerRecord(name="H", previous_position=4),
        PlayerRecord(name="I", previous_position=6),
        PlayerRecord(name="J", previous_position=8),
        PlayerRecord(name="K", previous_position=1),
    ]


def with_size(size):
    list_of_previous_positions = list(range(size))
    random.shuffle(list_of_previous_positions)
    player_records = []
    for previous_position in list_of_previous_positions:
        player_records.append(PlayerRecord(name=str(previous_position + 1), previous_position=previous_position + 1))
    return player_records
