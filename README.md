# BirthdayReminderApp
# TO UPDATE by 2022/06/24
cron job - 52 20 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/test_data.csv 1 >> Public/output.txt
crontab -e - 10 12 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python  main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/test_data.csv 2 >> Public/output.txt
crontab -e -> 46 12 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python  main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/data.csv 2 >> Public/birthdays.txt

Tests run as in terminal:
python -m pytest Tests/tests.py
 mypy and pyflakes
