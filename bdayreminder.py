#!/usr/bin/python3

# Main Python file for Birthday Reminder Application
# Created by Aurimas A. Nausedas on 06/18/22.
# Uploaded by Aurimas A. Nausedas on 06/20/22.
# Updated by Aurimas A. Nausedas on 06/23/22.
# Updated by Aurimas A. Nausedas on 06/26/22.
# Updated by Aurimas A. Nausedas on 06/29/22.
# Updated by Aurimas A. Nausedas on 07/05/22.

import re
from datetime import datetime, timedelta
import csv
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv  # type:ignore
load_dotenv()


USR = os.getenv('USR')
PSW = os.getenv('PSW')
# global variable used anywhere
DATE_AFTER_SEVEN_DAYS = (datetime.now().date() + timedelta(days=7)).strftime('%m-%d')


def validate_data_and_send_emails(input_file, send_emails=False) -> None:
    """
    Checking validity of an input_file and whether birthday or birthdays are in a week.
    Then appending lists and sending the respective emails if there is at least one birthday in a week.
    :param input_file: object
    :param send_emails: bool
    :return:
    """
    list_of_birthdays_in_a_week = []
    list_to_send = []
    birthday_in_a_week = DATE_AFTER_SEVEN_DAYS
    if not os.path.exists(input_file):
        raise Exception('ERROR file doesn\'t exist')
    elif input_file.endswith('csv'):
        try:
            with open(input_file) as csv_file:
                opened_file = csv.reader(csv_file)
                next(opened_file)
                for idx, item in enumerate(opened_file):
                    try:
                        result_parsed_date = parse_date(item[2])
                        parsed_date = result_parsed_date['value']
                        fmt = result_parsed_date['format']
                        # print(fmt)
                        # parsed_date[], fmt = parse_date(item[2])['value']
                        # # print(parsed_date)
                        # # print(type(parsed_date))
                        if is_valid_input(fmt, item, idx, not send_emails) is True:
                            if parsed_date and parsed_date.strftime('%m-%d') == birthday_in_a_week:
                                list_of_birthdays_in_a_week.append(item)
                            else:
                                list_to_send.append(item)
                    except Exception as error:
                        sys.stderr.write(f'ERROR for {item} : {error}\n')
                if send_emails:
                    send_multiple_emails(list_of_birthdays_in_a_week, list_to_send)
        except Exception as error:
            sys.stderr.write(f'Malformed csv file : {error}\n')
    else:
        raise Exception('ERROR: Wrong data format file')


def parse_date(date) -> dict:
    """
    Parsing the input of a date. Returns datetime if succesful while string if unsuccesful
    :param date: str
    :return: dict
    """
    # print(date)
    is_parsed = False
    for fmt in ('%Y-%m-%d', '%m-%d'):
        try:
            result = {'value': datetime.strptime(date, fmt), 'format': fmt}
            is_parsed = True
        except ValueError:
            if not is_parsed:
                result = {'value': 'Wrong format', 'format': None}
    return result

    # for fmt in ('%Y-%m-%d', '%m-%d'):
    #     try:
    #         return {
    #             'isError': False,
    #             'value': datetime.strptime(date, fmt),
    #             'format': fmt
    #         }
    #     except ValueError:
    #         return {
    #             'isError': True,
    #             'value': 'Wrong format',
    #             'format': None
    #         }

    # return f'ERROR: Wrong format', None
    # if fmt  == '%Y-%m-%d':
    #     return datetime.strptime(date, fmt), fmt
    # elif fmt == '%m-%d':
    #     return datetime.strptime(date, fmt), fmt

def is_valid_input(fmt, item, idx, to_print) -> bool:
    """
    Validating inputs of items provided from data file.
    :param fmt: str
    :param item: str
    :param idx: int
    :param to_print: bool
    :return: bool
    """
    res = False
    error_message = None
    if fmt is None:
        error_message = f'ERROR: Invalid date for {item[0]} at row {idx+2}. Date given is {item[2]} '
    elif not is_date_in_past(item[2], fmt):
        error_message = f'ERROR: Date is in the future for {item[0]} at row {idx+2}. Date given is {item[2]} '
    elif item[0] != "":
        error_message = f'ERROR: Empty name field is for email {item[1]} at row {idx+2} '
    elif not is_valid_email(item[1]):
        error_message = f'ERROR: Invalid email for {item[0]} at row {idx+2} '
    else:
        res = True

    if to_print and error_message is not None:
        sys.stderr.write(f'{error_message}\n')

    return res


def send_multiple_emails(birthday_individuals, to_send) -> None:
    """
    Sending emails to every recipient of the to_send list and not to the list of birthday_individual persons.
    Defining variables and passing the items of a list to send_email function.
    :param birthday_individuals: list
    :param to_send: list
    :return:
    """
    days_left = '7 day'
    today = datetime.now().date()
    future_date = (today + timedelta(days=7)).strftime('%m-%d')
    for bday in birthday_individuals:
        sys.stdout.write(f'{bday[0]} will have birthday in a week.\n')
        for item in to_send:
            send_email(item[0], bday[0], future_date, days_left, item[1])
    sys.stdout.write('Emails sent successfully.\n')


def is_date_in_past(date, date_format) -> bool:
    """
    Looking if date is in the past.
    :param date: str
    :param date_format: str
    :return: bool
    """
    now = datetime.now().date()
    is_past = True
    # print(date,date_format)
    if date_format == '%Y-%m-%d':
        if datetime.strptime(date, date_format).date() < now:
            is_past = True
        else:
            is_past = False
    return is_past


# def contains_name(name) -> bool:
#     """
#     Checking if the input of a name column of a csv file contains something or not.
#     :param name: str
#     :return: bool
#     """
#     return name != ''


def is_valid_email(email) -> bool:
    """
    Checking through regex if an email is valid.
    :param email: str
    :return: bool
    """
    regex = r'^[a-zA-Z0-9]+[\._]?[ a-zA-Z0-9]+[@]\w+[. ]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


def send_email(name, bday_name, bday_date, days_left, to_email) -> None:
    """
    Sending an email to one recipient from the csv file by defining an SMTP client session object.
    :param name: str
    :param bday_name: str
    :param bday_date: str
    :param days_left: str
    :param to_email: str
    :return:
    """
    message = f'Hi {name},\n\nThis is a reminder that {bday_name}\'s will be celebrating their birthday on ' \
              f'{bday_date}s.\n\nThere are {days_left}s left to get a present!\n'
    msg = MIMEMultipart()
    msg['Subject'] = f'Birthday Reminder: {bday_name}s\'s birthday on {bday_date}s'
    msg['From'] = USR
    msg['To'] = to_email
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    for i in range(2):
        try:
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(USR, PSW)
            mailserver.sendmail(USR, to_email, msg.as_string())
            break
        except Exception:
            continue
    mailserver.quit()


def run(read_path, cron_value) -> None: # geresni pavadinima sugalvoti
    """
    Inputting the path of a csv data file and running the script without having to input the choices as they are passed.
    :param read_path: object
    :param cron_value: int or str
    :return:
    """
    if cron_value.isdigit() and int(cron_value) == 1:
        validate_data_and_send_emails(read_path, send_emails=False)
    elif cron_value.isdigit() and int(cron_value) == 2:
        validate_data_and_send_emails(read_path, send_emails=True)
    else:
        sys.stdout.write(
            'Choose 1 to validate if input data file is correct or 2 to check for '
            'upcoming birthdays and send respective emails\n')
        choose_options(read_path)


def choose_options(read_path) -> None:
    """
    Asking for input and choosing what to run.
    :param read_path: object
    :return:
    """
    i = input()
    if i.isdigit() and int(i) == 1:
        validate_data_and_send_emails(read_path, send_emails=False)
    elif i.isdigit() and int(i) == 2:
        validate_data_and_send_emails(read_path, send_emails=True)
    else:
        sys.stdout.write('Please choose either 1 or 2\n')
        choose_options(read_path)


if __name__ == '__main__':
    arg_path = sys.argv[1]
    cron_input = sys.argv[2]
    run(arg_path, cron_input)
