from numb3rs import validate

def test_valid():
    assert validate('255.255.255.255')

def test_invalid():
    assert not validate('512.255.255.255')
    assert not validate('1000.2.3.2')
    assert not validate('299.21.3.2')
    assert not validate('200.2009.22.22')
    assert not validate('200.255.299.22')
    assert not validate('122.255.25.300')


