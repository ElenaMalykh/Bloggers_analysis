# content of test_expectation.py
import pytest
from helper_function.helper_function import *


@pytest.mark.parametrize("input_date,expected",
                         [("1 July, 2021", 7),
                         ("18 August, 2021", 8),
                          ("14 September, 2021", 9)])
def test_get_month(input_date, expected):
    assert get_month(input_date) == expected

@pytest.mark.parametrize("input_date,expected",
                         [("1 July, 2021", 2021),
                         ("18 August, 2022", 2022)])
def test_get_year(input_date, expected):
    assert get_year(input_date) == expected


@pytest.mark.parametrize("input_string, expected",
                        [("telegram_bloggers", "telegram"),
                         ("youtube_bloggers", "youtube"),
                         ("instagram_bloggers", "instagram")])
def test_get_blogger_category(input_string, expected):
    assert get_blogger_category(input_string) == expected

