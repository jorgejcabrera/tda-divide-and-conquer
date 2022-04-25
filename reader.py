from player.player_record import PlayerRecord


class Reader:

    def __init__(self, path):
        self.path = path

    def read(self):
        file = open(self.path)
        ranking = []
        for line in file:
            players = line.replace('\n', '').split(sep="|")
            for player in players:
                if player != '':
                    data = player.split(",")
                    ranking.append(PlayerRecord(name=data[0].replace(' ', ''), previous_position=data[1].replace(' ', '')))
        file.close()
        return ranking
