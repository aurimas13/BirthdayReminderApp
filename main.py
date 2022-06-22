#!/usr/bin/python3

# Python program For Birthday Reminder Application

# Importing Regex
import re

# Importing time modules
from datetime import datetime, timedelta

# Importing csv, os & sys
import csv
import os
import sys

# Setting email proxies
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Importing Union type
from typing import Union, Any

# Setting environment variables:
from dotenv import load_dotenv  # type:ignore

load_dotenv()
USR = os.getenv('USR')
PSW = os.getenv('PSW')
USR_ALT = os.getenv('USR_ALT')
PSW_ALT = os.getenv('PSW_ALT')


def birthday_file(file_path):
    """
    Converting a path of data file to the csv format that can be read.

    :param file_path:
    :return: object
    """
    try:
        file_name = open(file_path, 'r')
        csv_reader = csv.reader(file_name)
        next(csv_reader)
        return csv_reader
    except Exception:
        sys.stdout.write('Wrong input data file')



def checkBirthdaysInAWeek(input_file, send_emails=False) -> None:
    """
    Checking validity of an input_file and whether a birthday is in a week.
    Then appending lists and sending the respective emails if there is at least one birthday in a week.

    :param input_file: object
    :param send_emails: bool
    :return: None
    """
    list_of_birthdays_in_a_week = []
    list_to_send = []
    csv_file = birthday_file(input_file)
    birthday_in_a_week = birthdate_in_7_days()

    for idx, item in enumerate(csv_file):
        try:
            parsed_date, fmt = try_parsing_date(item[2])
            if is_valid_input(fmt, item, idx, not send_emails) is True:
                if parsed_date and parsed_date.strftime('%m-%d') == birthday_in_a_week:
                    list_of_birthdays_in_a_week.append(item)
                else:
                    list_to_send.append(item)
        except Exception as error:
            sys.stderr.write(f'ERROR for {item} : {error}\n')
    if send_emails:
        multiple_email_sends(list_of_birthdays_in_a_week, list_to_send)


def birthdate_in_7_days() -> str:
    """
    Find if there are any birthdays in a week
    :return: str
    """
    today = datetime.now().date()
    return (today + timedelta(days=7)).strftime('%m-%d')


def try_parsing_date(date) -> Union[Any, Any]:
    """
    Parsing the input of a date.

    :param date: str
    :return: datetime or dict, str or None
    """
    for fmt in ('%Y-%m-%d', '%m-%d'):
        try:
            return datetime.strptime(date, fmt), fmt
        except ValueError:
            pass
    return {'ERROR': 'Wrong format'}, None


def is_valid_input(fmt, item, idx, to_print) -> bool:
    """
    Validating inputs of items provided.

    :param fmt: str
    :param item: str
    :param idx: int
    :param to_print: bool
    :return: bool
    """
    res = False
    error_message = None
    if fmt is None:
        error_message = f'ERROR: Invalid date for {item[0]} at row {idx}. Date given is {item[2]} '
    elif not is_date_in_past(item[2], fmt):
        error_message = f'ERROR: Date is in the future for {item[0]} at row {idx}. Date given is {item[2]} '
    elif not is_not_empty_name(item[0]):
        error_message = f'ERROR: Empty name field is for email {item[1]} at row {idx} '
    elif not is_valid_email(item[1]):
        error_message = f'ERROR: Invalid email for {item[0]} at row {idx} '
    else:
        res = True

    if to_print and error_message is not None:
        sys.stderr.write(f'{error_message}\n')

    return res


def multiple_email_sends(birthday_individuals, to_send) -> None:
    """
    Sending emails to every recipient of the to_send list and not to the list of birthday_individual persons.
    Defining variables and passing the items of a list to send_email function.

    :param birthday_individuals: list
    :param to_send: list
    :return:
    """
    days_left = 7
    today = datetime.now().date()
    future_date = (today + timedelta(days=7)).strftime('%m-%d')
    for bday in birthday_individuals:
        sys.stdout.write(f'{bday[0]} will have birthday in a week.\n')
        for item in to_send:
            send_email(item[0], bday[0], future_date, days_left, item[1])


def is_date_in_past(date, date_format) -> bool:
    """
    Looking if date is in the past.

    :param date: str
    :param date_format: str
    :return:
    """
    now = datetime.now().date()
    is_past = True
    if date_format == '%Y-%m-%d':
        if datetime.strptime(date, date_format).date() < now:
            is_past = True
        else:
            is_past = False
    return is_past


def is_not_empty_name(name) -> bool:
    """
    Checking if the input of a name column of csv file is not empty.

    :param name: str
    :return: bool
    """
    if name == '':
        return False
    return True


def is_valid_email(email) -> bool:
    """
    Checking through regex if an email is valid.

    :param email: str
    :return: bool
    """
    regex = '^[a-zA-Z0-9]+[\._]?[ a-zA-Z0-9]+[@]\w+[. ]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


def send_email(name, birthday_name, bday_date, days_left, to_email):
    """
    Sending an email to one recipient from the csv file by defining an SMTP client session object.

    :param name: str
    :param birthday_name: str
    :param bday_date: str
    :param days_left: int
    :param to_email: str
    :return: bool
    """
    message = f'Hi {name}, This is a reminder that {birthday_name}\'s will be celebrating their birthday on {bday_date}\'s. There are {days_left}s left to get a present!'
    msg = MIMEMultipart()
    msg['From'] = USR_ALT
    msg['To'] = to_email
    msg['Subject'] = f'Birthday Reminder: {birthday_name}\'s birthday on {bday_date}\'s'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    for i in range(2):
        try:
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(USR_ALT, PSW_ALT)
            mailserver.sendmail(USR_ALT, to_email, msg.as_string())
            break
        except Exception:
            continue
    mailserver.quit()


def options(read_path, cron) -> None:
    """
    Choosing how to use the Python script.

    :param read_path: object
    :param cron: int or str
    :return: None
    """
    if cron.isdigit() and int(cron) == 1:  # aprasyti README
        checkBirthdaysInAWeek(read_path, send_emails=False)
    elif cron.isdigit() and int(cron) == 2:  # aprasyti README
        checkBirthdaysInAWeek(read_path, send_emails=True)
    else:  # aprasyti README
        sys.stdout.write(
            'Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails\n')
        i = int(input())
        if i == 1:
            checkBirthdaysInAWeek(read_path, send_emails=False)
        elif i == 2:
            checkBirthdaysInAWeek(read_path, send_emails=True)
        else:
            sys.stdout.write('Please choose either 1 or 2\n')
            options(read_path, cron)


if __name__ == '__main__':
    arg_path = sys.argv[1]
    cron = sys.argv[2]
    options(arg_path, cron)
