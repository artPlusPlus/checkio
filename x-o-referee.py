def checkio(game_result):
    def _check_candidates(candidates):
        for side in ['X', 'O']:
            if any([c for c in candidates if c == side*3]):
                return side
    
    result = _check_candidates(game_result)
    if result:
        return result

    columns = [''.join([row[col] for row in game_result]) for col in range(0, 3)]
    result = _check_candidates(columns)
    if result:
        return result
    
    diagonals = [''.join([game_result[r][c] for r, c in zip(range(0, 3), range(0, 3))]),
                 ''.join(game_result[r][c] for r, c in zip(range(0, 3), range(2, -1, -1)))]
    result = _check_candidates(diagonals)
    if result:
        return result

    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

