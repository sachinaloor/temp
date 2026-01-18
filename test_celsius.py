from celsius import celsius_to_fahrenheit

def test_freezing_point():
    assert round(celsius_to_fahrenheit(0),2) == 32