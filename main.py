from src.morpion import Morpion
from src.player import Player
from src.bot import Bot


name_1 = "user"
is_bot_1 = False

name_2 = "bot"
is_bot_2 = True

game = Morpion(Player(name_1, is_bot_1, "O"), Player(name_2, is_bot_2, "X"))

if is_bot_1 or is_bot_2:
    bot = Bot()

player = name_1
while not (game.is_full() or game.is_winner()):
    game.display_board()
    
    if game.get_player(player).get_is_bot():
        game.play(player, bot.get_play_index(game))
    
    else:
        game.play(player, game.request_user(player))
    
    if player == name_1:
        player = name_2
    else: player = name_1