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


def checkTodaysBirthdays(filePath):
    fileName = open(filePath, 'r')
    today = datetime.now().date().strftime('%m-%d')
    csvreader = csv.reader(fileName)
    next(csvreader)

    now = datetime.now().date()
    todays_birthdays = []
    for item in csvreader:
        try:
            parsed_date, fmt = try_parsing_date(item[2])
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
                if parsed_date and parsed_date.strftime('%m-%d') == time.strftime('%m-%d'):
                    birthday_name = item[0]
                    birthday_date = time.strftime('%m-%d')
                    print('hi')
                    print(birthday_date)
                    # days_until_birthday = birthday_date - now
                    # print(days_until_birthday)
                    # print(birthday_calculation_before_a_week(item[2]))
                    print(f'{birthday_name} has birthday today')
                    todays_birthdays.append(item)

            # send_email(item[0],birthday_name,today,birthday_date,user[1])
        except Exception as error:
            print(item, error)

    print(todays_birthdays)
    return todays_birthdays

# def send_emails(name):
#     for i in  checkTodaysBirthdays()

def birthday_calculation_before_a_week(date):
    subtract = date - timedelta(days=7)
    if subtract == 7:
        return True
    else:
        return False


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

def send_email(name,birthday_name,date,birthday_date,to_email):
    msg = MIMEMultipart()
    msg['From'] = USR
    msg['To'] = to_email
    msg['Subject'] = 'Trial'
    message = f'Hi {name}, This is a reminder that {birthday_name}\'s will be celebrating their birthday on {date}\'s. There are {birthday_date}\'s left to get a present!'
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
    # date_2 = '2022-06-18'
    checkTodaysBirthdays(sys.argv[1])
    # print(is_date_in_past(date_2, '%Y-%m-%d'))
    # print(datetime.now().strftime('%m-%d'))
    # email = 'ryan@one.lt'
    # email2 = 'anna..def@higgins.com'
    # print(is_valid_email(email))
    # print(is_valid_email(email2))
    # emails = ["mike@someAddress.org", "someone@gmail.com"]
    # subject = "Test email from Python"
    # body_text = "Python rules them all!"
    # send_email(subject, body_text, emails)
    print(datetime.now().date().strftime('%m-%d'))
    # send_email("Aurimas", 'Guga', 21, 21)
    print(PSW)
    seven_days = datetime.now().date()-timedelta(days=7)
    print(seven_days)
