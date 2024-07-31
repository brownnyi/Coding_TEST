def solution(players, callings):
    players_rank = {j:i for i, j in enumerate(players)}

    for call in callings:
        current_rank = players_rank[call]

        players_rank[call] -= 1
        players_rank[players[current_rank - 1]] += 1

        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]

    return players