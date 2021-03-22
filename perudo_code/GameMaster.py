from Game import Game

class GameMaster:
    
    def __init__(self, player_names):
        self.game = Game(player_names)
        
        print('Game started. ')
        self.play()
        
    def play(self):
        
        while self.game.get_player_number() > 1:
            print('On round {}, We play with {} amazing players: {}'.format(
                self.game.get_round(), 
                self.game.get_player_number(), 
                self.game.print_player_names())
            )
            
            current_player = self.game.get_next_player()
            print('{}\'s turn. Here are your dice: {}.'.format(current_player.get_name(), current_player.display_dice()))
            
            if self.game.get_round() >= 10:
                break
                
            self.game.set_next_player()
                
        print('Game over.')
            
        
if __name__ == '__main__': 
    gm = GameMaster(['Carlotta', 'Toine', 'Flago'])