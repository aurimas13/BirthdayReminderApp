# Python program For Birthday Reminder Application
import re
import time
from datetime import datetime
import csv
import os
import smtplib
import sys

from configparser import ConfigParser
# Setting environment variables:
USER = os.getenv('USER')
PASSWORD = os.environ.get('PSW')


def checkTodaysBirthdays(filePath):
    fileName = open(filePath, 'r')
    today = datetime.now().date().strftime('%m-%d')
    csvreader = csv.reader(fileName)
    next(csvreader)

#     body = f'Subject: Birthday Reminder: {item[0]}\'s birthday on {item}%(date)s
# Body:
# Hi %(name)s,
# This is a reminder that %(name_of_birthday_person)s will be celebrating their
# birthday on %(date)s.
# There are %(amount_of_days)s left to get a present!'
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
                    print(f'{item[0]} has birthday today')
                    todays_birthdays.append(item)
        except Exception as error:
            print(item, error)

    print(todays_birthdays)
    return todays_birthdays


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

def send_email(name, ):
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    msg = MIMEMultipart()
    msg['From'] = 'aurimas.nausedas@gmail.com'
    msg['To'] = 'aurimas.nausedas@gmail.com'
    msg['Subject'] = 'Trial'
    message = f'Hi {name}, This is a reminder that {birthday_name}\'s will be celebrating their birthday on {date}\'s. There are {date-birthday_date}\'s left to get a present!'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(USER, PASSWORD)

    mailserver.sendmail(USER,'aurimas.nausedas@gmail.com',msg.as_string())

    mailserver.quit()


# def send_email(subject, body_text, emails):
#     """
#     Send an email
#     """
#     base_path = os.path.dirname(os.path.abspath('/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp
# '))
#     config_path = os.path.join(base_path, "email.ini")
#     if os.path.exists(config_path):
#         cfg = ConfigParser()
#         cfg.read(config_path)
#     else:
#         print("Config not found! Exiting!")
#         sys.exit(1)
#     host = cfg.get("smtp", "server")
#     from_addr = cfg.get("smtp", "from_addr")
#     BODY = "\r\n".join((
#             "From: %s" % from_addr,
#             "To: %s" % ', '.join(emails),
#             "Subject: %s" % subject ,
#             "",
#             body_text
#             ))
#     server = smtplib.SMTP(host)
#     server.sendmail(from_addr, emails, BODY)
#     server.quit()


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
