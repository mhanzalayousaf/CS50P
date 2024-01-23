from bank import value


def test_greeting_lowercase():
    assert value("hello world") == 0
    assert value("hi world") == 20
    assert value("wassup world") == 100


def test_greeting_uppercase():
    assert value("HELLO WORLD") == 0
    assert value("HI WORLD") == 20
    assert value("WASSUP WORLD") == 100