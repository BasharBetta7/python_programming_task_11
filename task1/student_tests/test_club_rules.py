from task1.club_rules import can_join_club
import pytest
#--------------------------
# Equivalence classes tests
#--------------------------




def test_mid_range_value():
    assert can_join_club(30, 200) is True

def test_small_age_rejected():
    assert can_join_club(15, 200) is False

def test_high_age_rejected():
    assert can_join_club(50, 200) is False

def test_low_balance_rejected():
    assert can_join_club(30, 50) is False

def test_low_balance_small_age_rejected():
    assert can_join_club(18, 90) is False


#--------------------------
# Boundary value tests
#--------------------------

def test_low_age_accepted():
    assert can_join_club(20, 200) is True

def test_high_age_accepted():
    assert can_join_club(40, 400) is True

def test_low_age_rejected():
    assert can_join_club(19, 200) is False

def test_high_age_rejected2():
    assert can_join_club(41, 200) is False

def test_low_balance_accepted():
    assert can_join_club(23, 100) is True

def test_low_balance_rejected2():
    assert can_join_club(23, 99) is False

    
