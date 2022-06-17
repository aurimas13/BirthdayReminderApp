# Python program For Birthday Reminder Application
import time
from datetime import datetime
import csv
import os
import pandas as pd
import csv
# rows = []
# with open("birthday_data.csv", "r") as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)

file = open('/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/birthday_data.csv')
csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)
rows = []
for row in csvreader:
    rows.append(row)
date_str = '2000-06-17'
for item in rows:
    # print(item[2])
    # if item[2] != '':
    try:
        # print(datetime.strptime(item[2], "%Y-%m-%d").strftime('%m-%d'))
        if datetime.strptime(item[2], '%Y-%m-%d').strftime('%m-%d') == time.strftime('%m-%d'):
            print(True)
        else:
            print(False)
    except Exception as error:
        print(item[2], error)

print(datetime.strptime(date_str, '%Y-%m-%d' ).strftime('%m-%d')) # formatting to month-day

# date_object = datetime.strptime(date_str, '%Y-%m-%d').strftime('%m-%d')
# print(type(date_object))
# print(date_object)  # printed in default formatting
file.close()

# col_list = ['first_name',  'last_name', 'clean_birth_date']
# df = pd.read_csv("/Users/aurimasnausedas/Documents/Python/birthdayApp/Clean_Player_Birthdays.csv", usecols=col_list)
# # df_2 = df.to_csv(index = False)
# print(df.head(7))
# df_2 = df.to_csv('birthday_data.csv', index=False)
# print(df_2)
# # print(df.loc[2]["clean_birth_date"])
# print(time.strftime(('%y%m%d')))
# birthdayFile = 'clean-player-birthda-advanced-visualization-sharing-in-data-world-QueryResult.csv'
def checkTodaysBirthdays(rows):
#     fileName = open(file_df, newline='', encoding='utf-8')
#     print(fileName)
#     if type(spreadsheet) == pd.core.frame.DataFrame:
#
    today = time.strftime('%m-%d')
    flag = 0
    for line in rows:
        if today in line:
            print(True)
        # else:
        #     print('Come on')
#            line = line.split(' ')
#            flag = 1
#            # line[1] contains Name and line[2] contains Surname
#            os.system('notify-send "Birthdays Today: ' + line[1]
#                      + ' ' + line[2] + '"')
#     if flag == 0:
#         os.system('notify-send "No Birthdays Today!"')
#
if __name__ == '__main__':
 checkTodaysBirthdays(rows)

# def checkBirthdays():
#     myBrthdayFile = '/Users/aurimasnausedas/Documents/Python/birthdayApp/birthdays.csv'
#     myBirthdayFileName = open(myBirthdayFile, 'r')
#     today = time.strftime('%m%d')
#     z = 0
# for i in myBirthdayFileName:
#     if today in i:
#        i = i.split(' ')
#        z =1
#        os.system('notify-send "Its the birthday of"' + i[1] + '_' + i[2])
#     if z == 0:
#        os.system('notify-send "Oh!No Birthday!"')
# if __name__ == '__main__':
#        checkBirthdays()
#
#
# def checkTodaysBirthdays():
#  fileName = open(birthdayFile, 'r')
#  today = time.strftime('%m%d')
#  flag = 0
#  for line in fileName:
#   if today in line:
#    line = line.split(' ')
#    flag = 1
#    # line[1] contains Name and line[2] contains Surname
#    os.system('notify-send "Birthdays Today: ' + line[1]
#              + ' ' + line[2] + '"')
#  if flag == 0:
#   os.system('notify-send "No Birthdays Today!"')