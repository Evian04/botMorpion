from src.morpion import Morpion
from src.player import Player
from src.bot import morpion_backtracking


name_1 = "user"
is_bot_1 = False

name_2 = "bot"
is_bot_2 = True

game = Morpion(Player(name_1, is_bot_1, "O"), Player(name_2, is_bot_2, "X"))

player = name_1
while not game.is_finished():
    game.display_board()
    
    if game.get_player(player).is_bot():
        game.play(player, morpion_backtracking(game, game.get_player(player)))
    
    else:
        game.play(player, game.request_user(player))
    
    if player == name_1:
        player = name_2
    else: player = name_1