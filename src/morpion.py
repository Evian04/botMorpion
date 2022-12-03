from player import Player


class Morpion:
    """
        This class serve to stock the morpion content and to do action like make someone play, or test if a player won.
    """
    def __init__(self, player_1: Player, player_2: Player):
        if player_1.get_name() == player_2.get_name():
            quit(f"Error at the __init__() function of class Morpion : the name of players must be different (name entered: {player_1.get_name()}")
        
        if player_1.get_name() == "Any" or player_2.get_name() == "Any":
            quit("Error at the `__init__()` function of the class Morpion : the name of a player cannot be 'Any'")

        self.player_1 = player_1
        self.player_2 = player_2
        self.grid = [str(d + 1) for d in range(9)] # ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    def request_user(self, player_name: str) -> int:
        # This function ask to the user in which cell he wants to play using the `input()` function, and return an integer between 0 and 8 inclusive
        user_input = input(f"{player_name}, enter the index of the place you want to play : ")
        if not user_input.is_digit() or not int(user_input) - 1 in range(9):
            print("You must enter a digit between 1 and 9 inclusive !")
            return self.request_user()
        
        return int(user_input) - 1

    def play(self, player_name: str, index: int):
        # This function put the sign of the player `player_name` in the cell with index = `index`
        if not index in range(9): # If `index` isn't between 0 and 8
            quit(f"Error at function `play()` : the index entered ({index}) is not between 0 and 8 (inclusive)")

        self.grid[index] = self.get_player(player_name).get_sign()

    def get_content(self) -> list[str]:
        return self.grid
    
    def get_empty_cell(self) -> list:
        # This function return a list that contains the index of all the empty cells of the grid
        empty_cells = []
        for i in range(9):
            if self.grid[i].isdigit():
                empty_cells.append(i)
        
        return empty_cells

    def get_player(self, player_name: str) -> Player:
        # Return some information about a player with the `Player` class according to his name
        if player_name == self.player_1.get_name():
            return self.player_1
            
        if player_name == self.player_2.get_name():
            return self.player_2
            
        quit(f"Error at function `get_player()` : {player_name} does not match with any player name")
        # This error happens when none of the player has the name `name_player`

    def is_full(self) -> bool:
        # return if the grid is full
        return len(self.get_empty_cell()) == 0

    def is_winner(self, player_name: str = "Any") -> bool:
        # This function return if the player `player_name` won, or if `player_name == "Any"`, if any player won
        list_threesomes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for threesome in list_threesomes:
            if self.test_threesome(threesome, player_name):
                return True
        
        return False
    
    def test_threesome(self, threesome: list, player_name: str) -> bool:
        # This function return if the value of three cells are equals to the sign of a certain player or if their are just equal if `player_name == "Any"`
        if player_name == "Any":
            ref_value = self.content[threesome[0]]
        
        else:
            ref_value = self.get_player(player_name).get_sign()
        
        for index_cell in threesome:
            if self.content[index_cell] != ref_value:
                return False
        
        return True

    def display_grid(self):
        # This function display the grid in the terminal
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