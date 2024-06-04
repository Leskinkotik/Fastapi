from app.controllers.math import inc, minus, power

def test_inc():
    assert inc(3) == 567890

def test_minus():
    assert minus(3) == 2   