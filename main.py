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

# Setting environment variables:
from dotenv import load_dotenv
load_dotenv()
USR = os.getenv('USR')
PSW = os.getenv('PSW')
USR_ALT = os.getenv('USR_ALT')
PSW_ALT = os.getenv('PSW_ALT')

def birthday_file(file_path):
    try:
        file_name = open(file_path, 'r')
        csv_reader = csv.reader(file_name)
        next(csv_reader)
        return csv_reader
    except:
        print('Wrong input data file')


def checkBirthdaysInAWeek(input_file, send_emails=False):
    csv_file = birthday_file(input_file)
    today = datetime.now().date()
    birthday_in_a_week = (today + timedelta(days=7)).strftime('%m-%d')
    list_of_birthdays_in_a_week = []
    list_to_send = []
    for idx, item in enumerate(csv_file):

        try:
            parsed_date, fmt = try_parsing_date(item[2])
            if is_valid_input(fmt, item, idx, not send_emails) is True:
                if parsed_date and parsed_date.strftime('%m-%d') == birthday_in_a_week:
                    birthday_name = item[0]
                    print(f'{birthday_name} will have birthday in a week')
                    list_of_birthdays_in_a_week.append(item)
                else:
                    list_to_send.append(item)

        except Exception as error:
            print(item, error)

    if send_emails:
        multiple_email_sends(list_of_birthdays_in_a_week, list_to_send)
    # return list_of_birthdays_in_a_week, list_to_send


def is_valid_input(fmt, item, idx, to_print):
    res = False
    error_message = None
    if fmt is None:
        error_message = f'ERROR: Invalid date for {item[0]} at row {idx}. Date given is {item[2]}'
    elif not is_date_in_past(item[2], fmt):
        error_message = f'ERROR: Date is in the future for {item[0]} at row {idx}. Date given is {item[2]}'
    elif not is_not_empty_name(item[0]):
        error_message = f'ERROR: Empty name field is for email {item[1]} at row {idx}'
    elif not is_valid_email(item[1]):
        error_message = f'ERROR: Invalid email for {item[0]} at row {idx}'
    else:
        res = True

    if to_print and error_message is not None:
        print(error_message)

    return res


def multiple_email_sends(birthday_individual, to_send):
    days_left = 7
    today = datetime.now().date()
    future_date = (today + timedelta(days=7)).strftime('%m-%d')
    for bday in birthday_individual:
        for item in to_send:
            send_email(item[0], bday[0], future_date, days_left, item[1])


def try_parsing_date(text):
    for fmt in ('%Y-%m-%d', '%m-%d'):
        try:
            return datetime.strptime(text, fmt), fmt
        except ValueError:
            pass
    return {'ERROR': 'Wrong format'}, None


def is_date_in_past(date, date_format):
    now = datetime.now().date()
    is_past = True
    if date_format == '%Y-%m-%d':
        if datetime.strptime(date, date_format).date() < now:
            # print("Date is valid.")
         is_past = True
        else:
         is_past = False
    return is_past


def is_not_empty_name(name):
    if name == '':
        return False
    return True


def is_valid_email(email):
    regex = '^[a-zA-Z0-9]+[\._]?[ a-zA-Z0-9]+[@]\w+[. ]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False


def send_email(name, birthday_name, bday_date, days_left, to_email):
    message = f'Hi {name}, This is a reminder that {birthday_name}\'s will be celebrating their birthday on {bday_date}\'s. There are {days_left}s left to get a present!'
    msg = MIMEMultipart()
    # msg['From'] = USR
    msg['From'] = USR_ALT
    msg['To'] = to_email
    msg['Subject'] = f'Birthday Reminder: {birthday_name}\'s birthday on {bday_date}\'s'
    msg.attach(MIMEText(message))

    # try:
    for i in range(2):
        try:
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            # mailserver.login(USR, PSW)
            mailserver.login(USR_ALT, PSW_ALT)
            # mailserver.sendmail(USR,to_email,msg.as_string())
            mailserver.sendmail(USR_ALT,to_email,msg.as_string())
            mailserver.quit()
        except:
            # reconnect
        else:
            break
    else:
        # we failed all the attempts
    #     print('success')
    # except Exception as e:
    #     print('fail', e)
    # mailserver.quit()


def options(read_path, cron):
    if cron.isdigit() and int(cron) == 1: # sutvarkyti sita
        checkBirthdaysInAWeek(read_path, send_emails=True)
    elif str(cron) != int() or int(cron) != 1: # sutvarkyti sita
        print('Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails')
        i = int(input())
        if i == 1:
            checkBirthdaysInAWeek(read_path, send_emails=False)
        elif i == 2:
            checkBirthdaysInAWeek(read_path, send_emails=True)
        else:
            print('Please choose either 1 or 2')
            options(read_path,cron)

if __name__ == '__main__':
    arg_path = sys.argv[1]
    cron = sys.argv[2]
    options(arg_path, cron)
