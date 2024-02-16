from twttr import shorten

def test_shorten_string():
    assert shorten("What's your nameA?") == "Wht's yr nm?"

def test_shorten_nonstring():
    assert shorten("123") == "123"

