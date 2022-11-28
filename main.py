from botMorpion.src.morpion import Morpion
from botMorpion.src.bot import Bot
from botMorpion.src.player import Player


game = Morpion(Player(False, "user"), Player(True, "bot"))

while not game.is_full():
    game.display_board()
    game.set_digit("user", input("In which cell do you wonna play ?"))