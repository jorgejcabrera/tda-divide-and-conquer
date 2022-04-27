import sys

from create_ranking import CreatePlayersRanking
from reader import Reader

if __name__ == '__main__':
    brute_force_enabled = False
    try:
        file_path = sys.argv[1]
        brute_force_enabled = sys.argv[2] == "by_brute_force"
    except:
        print("Taking default ranking file")
        file_path = "ranking.txt"

    raking = Reader(file_path).read()
    useCase = CreatePlayersRanking()

    if brute_force_enabled:
        print("Using brute force strategy")
        rankings = useCase.execute_by_divide_and_conquer(raking)
    else:
        print("Using divide and conquer strategy")
        rankings = useCase.execute_by_divide_and_conquer(raking)

    print(rankings)
