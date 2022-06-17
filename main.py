def checkTodaysBirthdays():
    fileName = open('/Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/birthday_data.csv', 'r')
    csvreader = csv.reader(fileName)
    today = time.strftime('%m-%d')
    flag = 0
    rows = []
    today_birthdays = []
    for row in csvreader:
        rows.append(row)
    for item in rows:
        try:
            if datetime.strptime(item[2], '%Y-%m-%d').strftime('%m-%d') == today:
                print(f'{item[0]} {item[1]} has birthday today')
                today_birthdays.append(item)
                # print(item)
                flag = 1
            elif flag == 0:
                os.system('notify-send "No Birthdays Today"')
            else:
                continue
        except Exception as error:
            print(item[2], error)

    return today_birthdays

if __name__ == '__main__':
 checkTodaysBirthdays()
