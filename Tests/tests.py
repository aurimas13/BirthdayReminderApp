# test_with_unittest.py

import pytest
from cryptography.exceptions import InvalidTag
from main import try_parsing_date, is_date_in_past, is_not_empty_name, is_valid_email

def test_correct_parsing_date_ymd():
    date = '1993-05-09'
    assert try_parsing_date(date) == try_parsing_date('1993-05-09')


def test_correct_parsing_date_md():
    date = '08-29'
    assert try_parsing_date(date) == try_parsing_date('08-29')


def test_is_date_in_past_old():
    date_old = '1990-07-09'
    assert is_date_in_past(date_old) == True


def test_is_date_in_past_future():
    date_future = '2990-07-09'
    assert is_date_in_past(date_future) == False


def test_is_not_empty_name_empty():
    empty = ''
    assert is_not_empty_name(empty) == False


def test_is_not_empty_name_full():
    name = 'Alex'
    assert is_not_empty_name(name) == True


def test_is_valid_email_good():
    good_email = 'andrius.kaniava@gmail.com'
    assert is_valid_email(good_email) == True


def test_is_valid_email_bad():
    bad_email = 'andy.whatever@gmail.one.yahoo.com'
    assert is_valid_email(bad_email) == False


def test_is_valid_email_invalid_string():
    with pytest.raises(InvalidTag, match=''):
        is_valid_email()

