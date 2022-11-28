class Player:
    def __init__(self, is_bot: bool, name: str):
        self.is_bot = is_bot
        self.name = name

    def get_is_bot(self) -> bool:
        return self.is_bot

    def get_name(self) -> str:
        return self.name