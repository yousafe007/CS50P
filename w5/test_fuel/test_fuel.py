from fuel import gauge, convert
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('a/b')
        convert('2/1')
        convert('2/-1')
        convert("1.5/3")
    assert convert('3/4') == 75


def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(89) == '89%'

