from Player import Player
from datetime import datetime

class Game:
    
    def __init__(self, player_names):
        '''
        Initializes a game. 
        
        Args: a list containing player names. 
        '''
        self.start_date = datetime.now()
        self.players = []
        for player_name in player_names:
            self.players.append(Player(player_name))
            
        self.current_player = 0
        self.rounds = 1
            
    def get_start_date(self):
        return self.start_date.strftime("%d/%m/%Y %H:%M:%S")
            
    def get_player_number(self):
        return len(self.players)
    
    def get_player_names(self):
        return [player.get_name() for player in self.players]
    
    def get_round(self):
        return self.rounds
    
    def print_player_names(self):
        return ', '.join(self.get_player_names())
    
    def get_next_player(self):
        return self.players[self.current_player]
    
    def set_next_player(self):
        if self.current_player == len(self.players) - 1:
            self.current_player = 0 
            self.rounds += 1
        else:
            self.current_player += 1
    
    def start_new_round(self):
        for p in self.players:
            print(p)
        