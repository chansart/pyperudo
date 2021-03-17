from Player import Player

p = Player('Marta')

def test_hand_length():
    assert len(p.dice) == 5
    
def test_hand_sum():
    assert sum(p.dice) <= 25
    
def test_dice_values():
    for die in p.dice:
        assert 1 <= die <= 6
    
