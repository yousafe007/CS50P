from um import count
import pytest

def test_convert():
    assert count('um')==1
    assert count('asdas asd um asd') == 1
    assert count('asdas asd Um asd') == 1
    assert count('Yummy')==0




