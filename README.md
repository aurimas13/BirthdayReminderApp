<p align=center>
  <img height="222px" src="https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/Logo/birthdaylogo.png"/>
</p>

<p align="center" > <b> Birthday Reminder Application </b> </p>
<br>
<p align=center>
  <a href="https://github.com/aurimas13/HackerRank-LeetCode/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/npm/l/express"></a>
  <a href="https://twitter.com/aurimasnausedas"><img alt="twitter" src="https://img.shields.io/twitter/follow/aurimasnausedas?style=social"/></a>
</p>

The program checks whether a person has a birthday in a week and optionally sends reminders to the rest of the group. It involves the necessary functionalities for validating the input and sending emails.
This repository contains **2** **modules** where [bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py) involves these functionalities while [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) tests the package. Please refer to [Requirements](#requirements) for importing libraries, packages and addtional modules before looking at the [Usage](#usage) of the app or [Functions](#functions), [Tests](#tests), [Cron Job](#cron-job) and other fields.

# Table of contents

[//]: # (- [Birthday Reminder App]&#40;#birthday-reminder-app&#41;)

- [Table of contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
- [Datasets](#datasets)
- [Tests](#tests)
- [Cron Job](#cron-job)
- [Public](#public)
- [Logo](#photo)
- [License](#license)

# Requirements

**Python 3.9.12** is required to properly execute package's modules, imported libraries and defined functions. Imports of several libraries like dotnet, csv, pytest and typing to name a few are also needed. Some required versions are found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/requirements.txt) while those that are not mentioned come with the required Python version.

# Usage

After the requirements are met, the app package is set at your directory and terminal is run you have four options (FYI module takes two arguments):
1) To allow yourself to run **validation** or **check & send** - the  second argument has to be **0** while the data used for <data_file_path> and example shown below was data_20.csv: 
```
>>> python bdayreminder.py <data_file_path> 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19

>>> python bdayreminder.py <data_file_path> 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
2) To run **validation** or **check & send** another way - the second argument has to be any **other number** or a **string** while the data used for <data_file_path> and example shown below was data_20.csv:

```
>>> python bdayreminder.py <data_file_path> 3
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 3
Please choose either 1 or 2
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19 

>>> python bdayreminder.py <data_file_path> versada
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> versada
Please choose either 1 or 2
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```

3) To **validate** birthday persons **data file** for errors set the second argument to be **1** while the data used for <data_file_path> and example shown below was data_20.csv:

```
>>> python bdayreminder.py <data_file_path> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
``` 
4) To **check** birthday persons **data file** and **send emails** set the second argument to be **1** while the data used for <data_file_path> and example shown below was data_20.csv:

```
>>> python bdayreminder.py <data_file_path> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```

# Functions

An overview of functions found inside a module - ***bdayreminder.py***:
- **birthday_file(file_path)** converts a data file (*file_path*) to the csv format that can be read.
- **check_birthdays_in_s_week(input_file, send_emails)** checks the validity of an *input_file* and whether a birthday is in a week as well as optionally sends the respective emails (*send_emails*).
- **birthdate_in_7_days()** finds the date for the upcoming birthdays in a week.
- **try_parsing_date(date)** parses the *date*.
- **is_valid_input(fmt, item, idx, to_print)** validates inputs (*fmt*,*item*,*idx*,*to_print*).
- **multiple_email_sends(birthday_individuals, to_send)** sends emails to recipients of *to_send* list.
- **is_date_in_past(date, date_format)** looks if *date* is in the past.
- **is_not_empty_name(name)** checks *name* is not empty.
- **is_valid_email(email)** checks if an email is valid.
- **send_email(name, bday_name, bday_date, days_left, to_email)** sends an email to a recipient (*name*,*to_email*) as a reminder of a birthday (*bday_name*,*bday_date*) in advance (*days_left*).
- **run(read_path, cron)** takes the csv data file and runs the script without as choices are passed as arguments (*read_path*,*cron*).
- **choose_options(read_path)** asks for input (*read_path*) and chooses option to run.

In depth explanations of the functions can be found inside a module - [bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py).

# Datasets

There are three possible datasets to use. These are [data_20](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_20.csv) of 20 recipients, [data_50](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_50.csv) of 50 recipients and [data_80](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_80.csv) of 80 recipients.

# Tests

An overview of functions found inside a module - [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py):
- *test_correct_parsing_date_ymd()* tests if the correct date is parsed.
- *test_correct_parsing_date_md()* tests if the correct date is parsed.
- *test_is_date_in_past_old()* tests if the old date is in the past.
- *test_is_date_in_past_future()* tests if the future date is in the past.
- *test_is_date_in_past_past_month_day()* tests if the old date is in the past.
- *test_is_not_empty_name_empty()* tests if name provided is empty.
- *test_is_not_empty_name_full()* tests if name provided is a string.
- *test_is_valid_email_good()* tests if the email address is valid.
- *test_is_valid_email_bad()* tests if the email address is invalid.
- *test_birthdate_in_7_days()* tests if the function is indeed after 7 days.

By navigating to where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held or to the folder where the [BirthdayReminderApp](https://github.com/aurimas13/BirthdayReminderApp#birthday-reminder-app) program is extracted one can run these commands:

[comment]: <> (For DocTest run this command in terminal:)

[comment]: <> (``` python)

[comment]: <> (> python -m doctest -v calculator.py)

[comment]: <> (```)
1) To check source files for errors in the project folder:
```
>>> pyflakes .
```

2) To check source files for errors in test file: 
```
>>> pyflakes tests.py
```

3) To check typing for test file:
``` 
>>> python -m pytest tests.py
```

# Cron Job

To build cron job in mac terminal run:
``` 
>>> crontab -e
```

The syntax for cronjob when entering terminal could look like this (cd to the directory where BirthdayReminderApp folder is & where Python is installed)
``` 
>>> 0 6 * * * cd <directory_app_path> && <python_source_code> main.py <data_file_path> 2
[Optional] >>> 0 6 * * * cd <directory_app_path> && <python_source_code> main.py <data_file_path> 2 >> Public/birthdays.txt
```

Syntax customization for Cron Job can be checked [here](https://crontab.guru/).
# Public

Public folder contains three files: 
- [birthdays.txt](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/birthdays.txt) - the output of a Cron Job after implementing the [Optional] command as given at [Cron Job](#cron-job).
- [todolist](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/todolist) - the TO DO List.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the Birthday Reminder Application can be found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/Photo/birthdaylogo.png).

# License

The MIT [LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)
