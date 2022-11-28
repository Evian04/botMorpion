from botMorpion.src.module.player import Player


class Morpion:
    """
    This class serve to stock the morpion content and to do action like set a digit, or test if someone won.
    """
    def __init__(self, player_1: Player, player_2: Player):
        if player_1.get_name() == player_2.get_name():
            quit(f"Error at the __init__() function of class Morpion : the name of players must be different (name entered: {player_1.get_name()}")
        
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = [str(d + 1) for d in range(9)]

    def set_digit(self, player_name: str, index: int):
        if not index in range(9): # If `index` isn't between 0 and 8
            quit(f"Error at function `set_digit()` : the index entered ({index}) is not between 0 and 8 (inclusive)")

        self.board[index] = self.get_player(player_name).get_sign()

    def get_content(self) -> list[str]:
        return self.board

    def get_player(self, player_name: str) -> Player:
        """ Return some information about a player according to his name """
        if player_name == self.player_1.get_name():
            return self.player_1
            
        if player_name == self.player_2.get_name():
            return self.player_2
            
        quit(f"Error at function `get_player()` : {player_name} does not match with any player name")

    def is_full(self) -> bool:
        for cell in self.get_content():
            if cell == " ":
                return False
        return True

    def is_winner(self, player_name: str) -> bool: pass
    def display_board(self): pass