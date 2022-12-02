class Player:
    def __init__(self, is_bot: bool, sign: str, name: str):
        self.is_bot = is_bot
        self.name = name
        self.sign = sign

    def get_is_bot(self) -> bool:
        return self.is_bot

    def get_name(self) -> str:
        return self.name
    
    def get_sign(self) -> str:
        return self.sign