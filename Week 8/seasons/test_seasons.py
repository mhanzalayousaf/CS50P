from seasons import check_birthdate
import pytest


def test_check_birthdate():
    assert check_birthdate("1999-10-07") == ("1999", "10", "07")
    assert check_birthdate("1999-1-07") == None
    assert check_birthdate("July 20, 1999") == None