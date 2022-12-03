from src.morpion import Morpion
from src.player import Player
from src.bot import morpion_backtracking


name_1 = "User"
is_bot_1 = False

name_2 = "Bot"
is_bot_2 = True

game = Morpion(Player(name_1, is_bot_1, "O"), Player(name_2, is_bot_2, "X"))

player = name_1
while not game.is_finished():
    game.display_grid()
    
    if game.get_player(player).is_player_bot():
        game_copy = game
        game.play(player, morpion_backtracking(game_copy, game.get_player(player))[1])
        game.display_grid()
    
    else:
        game.play(player, game.request_user(player))
    
    player = game.get_other_player(player).get_name()
    print(player)

game.display_grid()