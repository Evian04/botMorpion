from morpion import Morpion
from player import Player


def morpion_backtracking(mrp: Morpion, player: Player) -> tuple(int):
    # This function return the best play to do
    empty_cells = mrp.get_empty_cells()

    best_play = (-2)

    for index in empty_cells:
        mrp.play(player.get_name(), index)

        if mrp.is_full():
            return (0, index)

        if mrp.is_winner(player.get_name()):
            return (1, index)

        result = morpion_backtracking(mrp, mrp.get_other_player(player.get_name()))
        if result[0] > best_play[0]:
            best_play = result
    
    return best_play