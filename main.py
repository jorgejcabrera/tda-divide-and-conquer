import sys

from create_ranking import CreatePlayersRanking
from reader import Reader

if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
    except:
        print("Taking default values")
        file_path = "ranking.txt"

    raking = Reader(file_path).read()
    useCase = CreatePlayersRanking()

    rankings = useCase.execute_by_divide_and_conquer(raking)

    print(rankings)
