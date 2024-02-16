from plates import is_valid

def test_1():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("AAA22A") == False
    assert is_valid("1.,") == False
    assert is_valid("AAA")
    assert is_valid("AAAAAA")

def test_2():

    assert not is_valid('1S05')
    assert not is_valid('PI3.14')
def test_3():
    assert not is_valid('CS05')
    assert not is_valid('OUTATIME')
    assert not is_valid('123')
    assert not is_valid('D')
def test_4():
    assert is_valid('CSJJA')
    assert is_valid("AA")
    assert not is_valid('+ABC')
    assert not is_valid("!?AB2*")





