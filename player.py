from computer import Computer


class Player:
    
    PLAYER_COUNTER = 2

    def __init__(self):
        self._player = ''
        
    def roll_player(self):

        while True:
            self._player = input('Please enter an option (scisors, paper, rock) ')

            if self._player.isdigit() == False and self._player in ('scisors', 'paper', 'rock'):
                return self._player
                break
            else:
                print('Error data type')
                
            
        #return self._player