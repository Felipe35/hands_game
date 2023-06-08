import random 


class Computer:
    
    COMPUTER_COUNTER = 2

    def __init__(self):
        self._computer = ''

    def _game_suits(self):
        return ('rock', 'scisors', 'paper')
    
    
    def roll_computer(self):
        self._computer += random.choice(self._game_suits())
        return self._computer
    
    def clear_roll(self):
        self._computer = str()