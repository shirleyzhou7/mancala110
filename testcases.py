from mancala import get_available_moves
from mancala import is_plyr_house
from mancala import is_end_match
from mancala import is_win
from mancala import get_pebble_coors
from mancala import switch_plyr
'''
def test_all():
    print("testing functions")
    test_avail_moves(
'''
def test_get_available_moves():
    print("testing get available moves")
    assert(get_available_moves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 0) == [0, 1, 2, 10, 11, 12])
    assert(get_available_moves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 1) == [3, 4, 5, 7, 8, 9])
    assert(get_available_moves([0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 23], 0) == [])
    assert(get_available_moves([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1) == [3])
    assert(get_available_moves([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0) == [])
    print("all done!")

def test_is_plyr_house():
    print("testing is_plyr_house")
    assert(is_plyr_house(0, 13) == False)
    assert(is_plyr_house(1, 8) == True)
    assert(is_plyr_house(0, 0) == True)
    assert(is_plyr_house(1, 6) == False)
    assert(is_plyr_house(0, 20) == False)
    print("all done!")

def test_is_end_match():
    print("testing is_end_match")
    assert(is_end_match([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 47]) == True)
    assert(is_end_match([0, 0, 0, 1, 0, 0, 20, 0, 0, 0, 0, 0, 0, 27]) == False)
    assert(is_end_match([0, 0, 0, 1, 0, 0, 28, 0, 0, 4, 0, 0, 0, 15]) == False)
    print("all done!")
    
def test_is_win():
    print("testing is_win")
    assert(is_win([0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 24]) == False)
    assert(is_win([0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 23]) == True)
    assert(is_win([0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 36]) == True)
    print("all done!")
    
def test_switch_plyr():
    print("testing test_switch_plyr")
    assert(switch_plyr([0, 6, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 17], 0) == 0)
    assert(switch_plyr([0, 2, 0, 0, 0, 0, 28, 0, 7, 0, 0, 0, 0, 12], 0) == 1)
    assert(switch_plyr([0, 1, 0, 2, 0, 0, 18, 0, 2, 0, 6, 0, 0, 20], 1) == 0)
    assert(switch_plyr([0, 0, 0, 0, 2, 3, 30, 0, 3, 0, 0, 0, 0, 10], 1) == 1)
    print("all done!")


