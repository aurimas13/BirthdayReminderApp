# test_with_unittest.py

# import pytest
# from cryptography.exceptions import InvalidTag
from datetime import datetime, timedelta
from main import try_parsing_date, is_date_in_past, is_not_empty_name, is_valid_email, birthdate_in_7_days


def test_correct_parsing_date_ymd():
    date = '1993-05-09'
    assert try_parsing_date(date) == try_parsing_date('1993-05-09')


def test_correct_parsing_date_md():
    date = '08-29'
    assert try_parsing_date(date) == try_parsing_date('08-29')


def test_is_date_in_past_old():
    date_old = '1990-07-09'
    date_format = '%Y-%m-%d'
    assert is_date_in_past(date_old, date_format) is True, 'Date should be older than today'


def test_is_date_in_past_future():
    date_future = '2990-07-09'
    date_format = '%Y-%m-%d'
    assert is_date_in_past(date_future, date_format) is False, "Correct date is in the past"


def test_is_date_in_past_past_month_day():
    date_future = '05-09'
    date_format = '%%m-%d'
    assert is_date_in_past(date_future, date_format) is True


def test_is_not_empty_name_empty():
    empty = ''
    assert is_not_empty_name(empty) is False, 'The name should be somthing'


def test_is_not_empty_name_full():
    name = 'Alex'
    assert is_not_empty_name(name) is True


def test_is_valid_email_good():
    good_email = 'andrius.kaniava@gmail.com'
    assert is_valid_email(good_email) is True


def test_is_valid_email_bad():
    bad_email = 'andy.whatever@gmail.one.yahoo.com'
    assert is_valid_email(bad_email) is False


def test_birthdate_in_7_days():
    now = datetime.now().date()
    assert birthdate_in_7_days() == (now + timedelta(days=7)).strftime("%m-%d")


# def test_is_valid_email_invalid_string():
#     with pytest.raises(InvalidTag):
#         is_valid_email(InvalidTag)
