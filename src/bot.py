class Morpion: pass
class Player: pass


def morpion_backtracking(mrp: Morpion, player: Player) -> tuple:
    # This function return the best play to do
    game = mrp
    empty_cells = game.get_empty_cells()

    best_play = (-2,)

    for index in empty_cells:
        game.play(player.get_name(), index)

        if game.is_full():
            return (0, index)

        if game.is_winner(player.get_name()):
            return (1, index)

        result = morpion_backtracking(game, game.get_other_player(player.get_name()))
        if result[0] > best_play[0]:
            best_play = result
    
    return best_play