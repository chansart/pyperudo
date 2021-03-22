from GameMaster import GameMaster

gm = GameMaster(['Carlotta', 'Toine', 'Flago'])

def test_parse_guess_correct():
    assert gm.parse_guess('2 5') == [2, 5]
    
def test_parse_guess_mix_int_and_str():
    assert gm.parse_guess('2 five') == None