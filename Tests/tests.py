# Test file for Birthday Reminder Application
# Created by Aurimas A. Nausedas on 06/21/22.
# Updated by Aurimas A. Nausedas on 06/23/22.

from datetime import datetime, timedelta
from bdayreminder import try_parsing_date, is_date_in_past, is_not_empty_name, is_valid_email, is_birthdate_in_7_days


def test_correct_try_parsing_date_ymd():
    """
    Testing if the correct date of Y-m-d is parsed.

    :assert: bool
    """
    date = '1993-05-09'
    assert try_parsing_date(date) == try_parsing_date('1993-05-09')


def test_correct_try_parsing_date_md():
    """
    Testing if the correct date of m-d is parsed.

    :assert: bool
    """
    date = '08-29'
    assert try_parsing_date(date) == try_parsing_date('08-29')


def test_is_date_in_past_old():
    """
    Testing if the old date of Y-m-d is truly in past.

    :assert: bool
    """
    date_old = '1990-07-09'
    date_format = '%Y-%m-%d'
    assert is_date_in_past(date_old, date_format) is True, 'Date should be older than today'


def test_is_date_in_past_future():
    """
    Testing if the future date of Y-m-d is in past.

    :assert: bool
    """
    date_future = '2990-07-09'
    date_format = '%Y-%m-%d'
    assert is_date_in_past(date_future, date_format) is False, "Correct date is in the past"


def test_is_date_in_past_past_month_day():
    """
    Testing if the old date of m-d is truly in past.

    :assert: bool
    """
    date_future = '05-09'
    date_format = '%%m-%d'
    assert is_date_in_past(date_future, date_format) is True


def test_is_not_empty_name_empty():
    """
    Testing if name provided is empty.

    :assert: bool
    """
    name = ''
    assert is_not_empty_name(name) is False, 'The name should be something'


def test_is_not_empty_name_full():
    """
    Testing if name provided is a string.

    :asssert: bool
    """
    name = 'Alex'
    assert is_not_empty_name(name) is True, 'The name should contain at least one character'


def test_is_valid_email_good():
    """
    Testing if the email address is valid.

    :assert: bool
    """
    good_email = 'andrius.kaniava@gmail.com'
    assert is_valid_email(good_email) is True, 'The provided email is invalid'


def test_is_valid_email_bad():
    """
    Testing if the email address is invalid.

    :return: False
    """
    bad_email = 'andy.whatever@gmail.one.yahoo.com'
    assert is_valid_email(bad_email) is False


def test_is_birthdate_in_7_days():
    """
    Testing if birthdate_in_7_days() is indeed after 7 days.

    :return: bool
    """
    now = datetime.now().date()
    assert is_birthdate_in_7_days() == (now + timedelta(days=7)).strftime("%m-%d")

