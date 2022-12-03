from src.player import Player
from src.bot import Bot


class Morpion:
    """
    This class serve to stock the morpion content and to do action like set a digit, or test if someone won.
    """
    def __init__(self, player_1: Player, player_2: Player):
        if player_1.get_name() == player_2.get_name():
            quit(f"Error at the __init__() function of class Morpion : the name of players must be different (name entered: {player_1.get_name()}")
        
        self.player_1 = player_1
        self.player_2 = player_2
        self.grid = [str(d + 1) for d in range(9)]
        
        if self.player_1.get_is_bot or self.player_2.get_is_bot():
            self.bot == Bot()
    
    def play(self, player_name: str):
        player = self.get_player(player_name)
        if player.get_is_bot():
            self.set_digit(player_name, self.bot.get_play_index(self))
        
        else:
            self.set_digit(player_name, self.request_user)
    
    def request_user(self) -> int:
        user_input = input("Enter the place you want to play : ")
        if not user_input.is_digit() or not int(user_input) - 1 in range(9):
            print("You must enter a digit between 1 and 9 inclusive !")
            return self.request_user()
        
        return int(user_input) - 1

    def set_digit(self, player_name: str, index: int):
        if not index in range(9): # If `index` isn't between 0 and 8
            quit(f"Error at function `set_digit()` : the index entered ({index}) is not between 0 and 8 (inclusive)")

        self.grid[index] = self.get_player(player_name).get_sign()

    def get_content(self) -> list[str]:
        return self.grid
    
    def get_empty_cell(self) -> list:
        empty_cells = []
        for i in range(9):
            if self.grid[i].isdigit():
                empty_cells.append(i)
        
        return empty_cells

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

    def display_grid(self):
        grid = self.get_content()
        print("\n+-------+")
        for index_line in range(3):
            line = "| "
            for index_cell in range(3):
                line += str(grid[index_line * 3 + index_cell])
                if not index_cell == 2:
                    line += " "
            
            print(line + " |")
        print("+-------+\n")