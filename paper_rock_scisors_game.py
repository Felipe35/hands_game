from computer import Computer
from player import Player



class Game:
    
    
    
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        
        
    def _get_rolls(self):
       # computer = self._computer.roll_computer()
        #player = self._player.roll_player()
        return (self._player.roll_player(), self._computer.roll_computer())
    
    def play(self):
        
        while True:
            self._play_ground()
            
            game_over = self._check_game_over()
            if game_over:
                break
            
    
    def _play_ground(self):
        self._print_round_wellcome()
        print()
        
        player, computer = self._get_rolls()
        #print(player, computer)
        self._show_hands(player, computer)
        
        if player == 'rock' and computer == 'rock':
            print("****It is a tie!****")
            #print(player, computer)
            self._computer.clear_roll()

        elif player == 'rock' and computer == 'paper':
            print('****Computer won round****')
            #print(player, computer)
            self._computer.clear_roll()
            self._counter_comp('-')
            self._counter_player('+')

        elif player == 'rock' and computer == 'scisors':
            print('****Player won round****')
            #print(player, computer)
            self._computer.clear_roll()
            self._counter_player('-')
            self._counter_comp('+')

        elif player == 'paper' and computer == 'rock':
            print('****Player won round****')
           #print(player, computer)
            self._computer.clear_roll()
            self._counter_player('-')
            self._counter_comp('+')

        elif player == 'paper' and computer == 'scisors':
            print('****Computer won round****')
            self._computer.clear_roll()
            self._counter_player('+')
            self._counter_comp('-')
            
        elif player == 'paper' and computer == 'paper':
            print('****It is a tie!****')
            self._computer.clear_roll()


        elif player == 'scisors' and computer == 'paper':
            print('****Player won round****')
            #print(player, computer)
            self._computer.clear_roll()
            self._counter_player('-')
            self._counter_comp('+')

        elif player == 'scisors' and computer == 'rock':
            print('****Computer won round****')
            #print(player, computer)
            self._computer.clear_roll()
            self._counter_player('+')
            self._counter_comp('-')

        elif player == 'scisors' and computer == 'scisors':
            print('****It is a tie!****')
            self._computer.clear_roll()
        print()
        self._show_scores()
                    
           
    def _check_game_over(self):
        if Computer.COMPUTER_COUNTER == 0:
            print("\n*********||Computer Won!||*********")
            return True
        elif Player.PLAYER_COUNTER == 0:
            print("\n*********||You Won!||*********")
            return True
        else:
            return False
    
    def _show_scores(self):
        print(f"Your score: {Player.PLAYER_COUNTER}")
        print(f"Computer score: {Computer.COMPUTER_COUNTER}")
      
    
    def _print_round_wellcome(self):
        print("\n------- New Round -------")
    
    def _show_hands(self, player_value, computer_value):
        print('==========================================')
        print(f"\nPlayer hand shows a: {player_value}")
        print(f"Computer hand shows a: {computer_value}\n")
        print('==========================================')
        
        
    def _counter_comp(self, value):
        if value == '+':
            Computer.COMPUTER_COUNTER += 1 
        elif value == '-':
            Computer.COMPUTER_COUNTER -= 1
      
    
    def _counter_player(self, value):
        if value == '+':
            Player.PLAYER_COUNTER += 1
        elif value == '-':
            Player.PLAYER_COUNTER -= 1
                
            
player = Player()
computer = Computer()
game = Game(player, computer)
game.play()