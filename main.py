from src.morpion import Morpion
from src.player import Player


name_player_1 = "user"
name_player_2 = "bot"
game = Morpion(Player(False, "O", name_player_1), Player(True, "X", name_player_2))

while not (game.is_full() or game.is_winner()):
    game.display_board()
    for name_player in [name_player_1, name_player_2]:
        game.play(name_player)