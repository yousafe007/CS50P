from working import convert
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('8:66 AM to 4:66 PM')
    with pytest.raises(ValueError):
        convert('8:60 AM 4:60 PM')
    assert convert('8:00 PM to 9:00 PM') == '20:00 to 21:00'
    assert convert('8:00 PM to 9:05 PM') == '20:00 to 21:05'

