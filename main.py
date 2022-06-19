# Python program For Birthday Reminder Application
import sys
import re
import time
from datetime import datetime
import os
import csv

def checkTodaysBirthdays(filePath):
    fileName = open(filePath, 'r')

    csvreader = csv.reader(fileName)
    next(csvreader)
    # today_date = datetime.now().strftime('%Y-%m-%d') #time.strftime('%m-%d')
    # print(today_date)
    # today_month = datetime.now().strftime('%m-%d')
    # print(today_month)
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


if __name__ == '__main__':
    # date_2 = '2022-06-18'
    checkTodaysBirthdays(sys.argv[1])
    # print(is_date_in_past(date_2, '%Y-%m-%d'))
    # print(datetime.now().strftime('%m-%d'))
    # email = 'ryan@one.lt'
    # email2 = 'anna..def@higgins.com'
    # print(is_valid_email(email))
    # print(is_valid_email(email2))
