from src.module.morpion import Morpion
from src.module.bot import Bot
from src.module.player import Player


game = Morpion(Player(False, "O", "user"), Player(True, "X", "bot"))

while not (game.is_full() or game.is_winner()):
    game.display_board()
    game.set_digit("user", input("In which cell do you wonna play ?"))