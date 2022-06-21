# Python program For Birthday Reminder Application
import re
import time
from datetime import datetime, date, timedelta
import csv
import os
import smtplib
import sys

from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Setting environment variables:
load_dotenv()
USR = os.getenv('USR')
PSW = os.getenv('PSW')


def checkBirthdaysInAWeek(filePath):
    fileName = open(filePath, 'r')
    today = datetime.now().date().strftime('%m-%d')
    csvreader = csv.reader(fileName)
    next(csvreader)

    today = datetime.now().date()
    birthday_in_a_week = (today + timedelta(days=7)).strftime('%m-%d')
    print(birthday_in_a_week)
    print(time.strftime('%m-%d'))
    list_of_birthdays_in_a_week = []
    list_to_sent = []
    list_bday_days = []
    for item in csvreader:

        try:
            parsed_date, fmt = try_parsing_date(item[2])
            # if not is_valid_input():
            if fmt is None:
                print({'Error': "Invalid date"})
            # elif valid_date(item[2], fmt) == True:
            elif not is_date_in_past(item[2], fmt):
                print({'Error': "Date is in the future"})
            elif not is_not_empty_name(item[0]):
                print({'Error': 'Empty name field'})
            elif not is_valid_email(item[1]):
                print({'Error': 'Invalid email'})
            else:
                if parsed_date and parsed_date.strftime('%m-%d') == birthday_in_a_week:
                    birthday_name = item[0]
                    print(f'{birthday_name} will have birthday in a week')
                    list_of_birthdays_in_a_week.append(item)
                    list_bday_days.append(birthday_in_a_week)
                    days_left = calculate_time_left(list_bday_days)
                    list_bday_days.append(days_left)
                else:
                    list_to_sent.append(item)

        except Exception as error:
            print(item, error)

    # print(list_of_birthdays_in_a_week)
    # print(list_to_sent)
    # print(list_bday_days[0])
    # print(list_bday_days[1])
    # print(calculate_time_left(list_bday_days))
    multiple_email_sends(list_of_birthdays_in_a_week, list_to_sent, list_bday_days)
    return list_of_birthdays_in_a_week, list_to_sent, list_bday_days

# def is_valid_input():

def calculate_time_left(birthdays_list):
    bday_to_be = datetime.strptime(birthdays_list[0], '%m-%d')
    current_date = datetime.now().date()
    year = current_date.year
    if current_date.month == 12 and current_date.day >= 25:
        year = current_date.year + 1
    d1 = date(year, current_date.month, current_date.day) # if year is 2022 but takes as 2023 as of todayeven though months are different like 23-01 - 22-12, it should calulcate this
    d2 = date(year, bday_to_be.month, bday_to_be.day) # if year is 2023 but it takes as 2023 :(
    delta = d2 - d1
    if delta.days == 7:
        return f"{delta.days} day" # Output should say 7 days
    else:
        print("Not any birthdays expected within a week") # Sitas nereikalingas nes niekada nebus call'inamas


def multiple_email_sends(birthday_individual, to_sent, days):
    # print(days[1])
    for bday in birthday_individual:
        for item in to_sent:
            send_email(item[0],bday[0],days[0],days[1],item[1])


def try_parsing_date(text):
    for fmt in ('%Y-%m-%d', '%m-%d'):
        try:
            return datetime.strptime(text, fmt), fmt
        except ValueError:
            pass
    return {'error': 'Wrong format'}, None


def is_date_in_past(date, format):
    now = datetime.now().date()
    isPast = True
    if format == '%Y-%m-%d':
        if datetime.strptime(date, format).date() < now:
            print("Date is valid.")
            isPast = True
        else:
            isPast = False
    return isPast


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

def send_email(name, birthday_name, date, days_left, to_email):
    msg = MIMEMultipart()
    msg['From'] = USR
    msg['To'] = to_email
    msg['Subject'] = f'Birthday Reminder: {birthday_name}\'s birthday on {date}\'s'
    message = f'Hi {name}, This is a reminder that {birthday_name}\'s will be celebrating their birthday on {date}\'s. There are {days_left}s left to get a present!'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(USR, PSW)

    mailserver.sendmail(USR,'aurimas.nausedas@gmail.com',msg.as_string())

    mailserver.quit()


if __name__ == '__main__':
    checkBirthdaysInAWeek(sys.argv[1])
    # i = '06-27'
    # # print(datetime.now().date().strftime('%m-%d'))
    # # seven_days = datetime.now().date()-timedelta(days=7)
    # # print(seven_days)
    # # print(datetime.strptime(seven_days, '%Y %m %d'))
    # d0 = datetime.strptime('01-01', '%m-%d')
    # d1 = datetime.strptime('2022-12-25', '%Y-%m-%d')
    # d2 = date(d1.year, d1.month,  d1.day)  # if year is 2022 but takes as 2023 as of todayeven though months are different like 23-01 - 22-12, it should calulcate this
    # d3 = date(d1.year, d0.month, d0.day)  # if year is 2023 but it takes as 2023 :(
    # delta = d3 - d2
    # print(delta.days)
