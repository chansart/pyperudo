from Game import Game

g = Game(['Carlotta', 'Toine', 'Flago'])

def test_player_names():
    assert g.get_player_names() == ['Carlotta', 'Toine', 'Flago']
    
def test_player_number():
    assert g.get_player_number() == 3