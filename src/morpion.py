from botMorpion.src.player import Player


class Morpion:
    def __init__(self, player1: Player, player2: Player): pass
    def set_digit(self, player_name: str, index: int): pass
    def is_full(self) -> bool: pass
    def is_winner(self, player_name: str) -> bool: pass
    def get_content(self) -> list[str]: pass
    def get_player(self, num: int) -> Player: pass
    def display_board(self): pass