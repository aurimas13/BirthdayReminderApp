# Python program For Birthday Reminder Application
import sys

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
            if valid_date(item[2], fmt) == True:
                if parsed_date and parsed_date.strftime('%m-%d') == time.strftime('%m-%d'):
                    print(f'{item[0]} has birthday today')
                    todays_birthdays.append(item)
            else:
                print({'error': "Invalid date"})
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
    return {'error': 'Wrong format'}
    # raise ValueError('no valid date format found')


def valid_date(date, fmt):
    if fmt == '%Y-%m-%d':
        isValidDate = True
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            print("Date is valid.")
        except ValueError:
            isValidDate = False
    elif fmt == '%m-%d':
        # month, day = date.split('-')
        isValidDate = True
        try:
            date = datetime.strptime(date, "%m-%d")
            print("Date is valid.")
        except ValueError:
            isValidDate = False
    return isValidDate



if __name__ == '__main__':
 checkTodaysBirthdays(sys.argv[1])
