import random

class Player: 
    
    def __init__(self, name, howManyDice=5):
        self.name = name
        self.num_dice = 5
        self.dice = self.rollingDice(howManyDice=5)
        
    def get_name(self):
        return self.name
    
    def display_dice(self):
        return self.dice
        
    def rollingDice(self, howManyDice):
        '''
        This function returns a list containing the values for player's dice
        
        Args: 
        - howManyDice: integer representing how many dice player is rolling
        
        Returns:
        - a list of dice values
        '''
        dice = []
        for i in range(howManyDice):
            dice.append(random.randint(1, 6))
            
        return sorted(dice)
    
    
if __name__ == '__main__':
    p = Player('Carlotta')
    print(p)
    print(p.dice)
