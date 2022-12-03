from player import Player
from morpion import Morpion


class Bot:
    """
        This class serve to calculates the better play to do in order to win using a backtracking function
    """
    def __init__(self): pass
    def is_winning(self, mrp: Morpion) -> int: pass
    def is_losing(self, mrp: Morpion) -> int: pass
    def backtracking(self, mrp: Morpion) -> int: pass
    def get_play_index(self, mrp: Morpion) -> int: pass