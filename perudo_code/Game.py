from Player import Player

class Game:
    
    def __init__(self, player_names):
        '''
        Initializes a game. 
        
        Args: a list containing player names. 
        '''
        self.players = []
        for player_name in player_names:
            self.players.append(Player(player_name))
            
    def get_player_number(self):
        return len(self.players)
    
    def get_player_names(self):
        return [player.get_name() for player in self.players]