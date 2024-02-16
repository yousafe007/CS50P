# Assuming your script is named myapp.py and the functions are imported accordingly
from seasons import to_minutes, parse_date, num_to_word
from datetime import date, timedelta
import pytest
import inflect



# Test for parse_date function
def test_parse_date():
    assert parse_date("2024-02-15") == (2024, 2, 15)
    assert parse_date("1990-12-31") == (1990, 12, 31)
    with pytest.raises(ValueError):
        parse_date("incorrect-date")

# Test for num_to_word function
def test_num_to_word():
    assert num_to_word(123) == "one hundred twenty-three"
    assert num_to_word(0) == "zero"
    assert num_to_word(1001) == "one thousand one"

# Test for to_minutes function
# This test requires calculating the difference between today and a given date
def test_to_minutes():
    today = date.today()
    ten_days_ago = today - timedelta(days=10)
    ten_days_minutes = 10 * 24 * 60
    p = inflect.engine()
    expected_output = p.number_to_words(ten_days_minutes, andword="")
    # Assuming YYYY-MM-DD format for ten_days_ago
    ten_days_ago_str = ten_days_ago.strftime("%Y-%m-%d")
    assert to_minutes(ten_days_ago_str) == expected_output

    # Test with future date (should return None)
    future_date = today + timedelta(days=1)
    future_date_str = future_date.strftime("%Y-%m-%d")
    assert to_minutes(future_date_str) is None

    # Test with invalid date format
    assert to_minutes("invalid-date-format") is None
