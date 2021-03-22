from Game import Game

class GameMaster:
    
    def __init__(self, player_names):
        self.game = Game(player_names)
        self.new_turn = True
        self.previous_guess = None
        self.dice_counter = None
        
    def play(self):
        
        while self.game.get_player_number() > 1:
            
            print('===========\nOn turn {}, We play with {} amazing players: {}'.format(
                self.game.get_turn(), 
                self.game.get_player_number(), 
                self.game.print_player_names())
            )
            
            current_player = self.game.get_next_player()
            print('{}\'s turn. {} dice in play. \nHere are your dice: {}.'.format(
                current_player.get_name(), 
                self.game.get_num_dice_in_play(),
                current_player.get_dice())
            )
            
            print(self.game.get_all_dice())
            
            guess = input('What is your guess? (type b for \'bluffing\', or # # if you guess something)\n')
            
            if guess == 'b':
                if self.new_turn:
                    print('You are the first player. You have to guess. Try again.')
                    continue
                else:
                    # check if bluffing or not !
                    continue
            
            else:
                parsed_guess = self.parse_guess(guess)
            
            
                
            print('You guessed: {}'.format(guess))
            
            if self.game.get_table_round() >= 10:
                break
                
            self.game.set_next_player()
                
        print('Game over.')
        
    def parse_guess(self, guess):
        try:
            return [int(i) for i in guess.split()]
        except ValueError:
            print('Unparseable guess. Try again. ')
            return None
        
if __name__ == '__main__': 
    gm = GameMaster(['Carlotta', 'Toine', 'Flago'])
    gm.play()