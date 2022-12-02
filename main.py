from src.morpion import Morpion
from src.bot import Bot
from src.player import Player


game = Morpion(Player(False, "O", "user"), Player(True, "X", "bot"))

while not (game.is_full() or game.is_winner()):
    game.display_board()
    game.set_digit("user", input("In which cell do you wonna play ?"))