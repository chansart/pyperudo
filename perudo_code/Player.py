import random

class Player: 
    
    def __init__(self):
        self.dice = self.rollingDice()
        
    def rollingDice(self, howManyDice=5):
        '''
        This function returns a list containing the values for player's dice
        
        Args: 
        - howManyDice: integer representing how many dice player is rolling
        
        Returns:
        - a list of dice values
        '''
        dice = []
        for i in range(howManyDice):
            dice.append(self.rollingDie())
            
        return dice   
        
    def rollingDie(self):
        '''
        This function returns one integer between 1 and 6. 
        
        Args: None
        
        Returns: integer
        '''
        return random.randint(1, 6)
    
    
if __name__ == '__main__':
    p = Player()
    print(p)
    print(p.dice)
