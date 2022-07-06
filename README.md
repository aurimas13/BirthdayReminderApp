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
- [Error](#errors)
- [Cron Job](#cron-job)
- [Public](#public)
- [Logo](#photo)
- [License](#license)

# Requirements

**Python 3.9.12** is required to properly execute package's modules, imported libraries and defined functions. Imports of several libraries like dotnet, csv and typing to name a few are also needed. Some required versions are found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/requirements.txt) while those that are not mentioned come with the used Python version.

# Usage
After the requirements are met, the app package is set at your directory and terminal is run you have four options<sup>1,2,3</sup>:
1) To allow yourself to run **validation** or **check & send** - the  second argument has to be any **other number**: 
```
>>> python bdayreminder.py <data_file_path> 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
'''
'''
>>> python bdayreminder.py <data_file_path> 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
2) To run **validation** or **check & send** another way - the second argument has to be any **other number**:

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
```

3) To **validate** birthday persons **data file** for errors set the second argument to be **1**:

```
>>> python bdayreminder.py <data_file_path> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
``` 
4) To **check** birthday persons **data file** and **send emails** set the second argument to be **2**:

```
>>> python bdayreminder.py <data_file_path> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
<br><sup>1</sup> **<data_file_path>** should look like this - Datasets/data_20.csv, but in your directory. The full path for me would be /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/data_20.csv </br>
<br><sup>2</sup> Main module takes two arguments when run from console. </br>
<br><sup>3</sup> The data used for examples was data_20.csv on 23<sup>th</sup> of June 2022.</br>

# Functions

An overview of functions found inside a module - ***bdayreminder.py***:

- **validate_data_and_send_emails(input_file, send_emails)** checks the validity of an *input_file* and whether a birthday is in a week as well as optionally sends the respective emails (*send_emails*).
- **parse_date(date)** parses the *date*.
- **is_valid_input(fmt, item, idx, to_print)** validates inputs (*fmt*,*item*,*idx*,*to_print*).
- **send_multiple_emails(birthday_individuals, to_send)** sends emails to recipients of *to_send* list.
- **is_date_in_past(date, date_format)** looks if *date* is in the past.
- **is_valid_email(email)** checks if an email is valid.
- **send_email(name, bday_name, bday_date, days_left, to_email)** sends an email to a recipient (*name*,*to_email*) as a reminder of a birthday (*bday_name*,*bday_date*) in advance (*days_left*).
- **run(read_path, cron)** takes the csv data file and runs the script without as choices are passed as arguments (*read_path*,*cron*).
- **choose_options(read_path)** asks for input (*read_path*) and chooses option to run.

[//]: # (- **convert_birthday_file&#40;file_path&#41;** converts a data file &#40;*file_path*&#41; to the csv format that can be read.)
[//]: # (- **is_birthdate_in_7_days&#40;&#41;** finds the date for the upcoming birthdays in a week.)
[//]: # (- **is_not_empty_name&#40;name&#41;** checks *name* is not empty.)

In depth explanations of the functions can be found inside a module - [bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py).

# Datasets

There are three possible datasets to use. These are [data_20](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_20.csv) of 20 recipients, [data_50](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_50.csv) of 50 recipients and [data_80](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Datasets/data_80.csv) of 80 recipients.

# Tests

An overview of functions found inside a module - [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py):
- *test_correct_parse_date_ymd()* tests if the correct date is parsed.
- *test_correct_parse_date_md()* tests if the correct date is parsed.
- *test_is_date_in_past_old()* tests if the old date is in the past.
- *test_is_date_in_past_future()* tests if the future date is in the past.
- *test_is_date_in_past_past_month_day()* tests if the old date is in the past.
- *test_is_valid_email_good()* tests if the email address is valid.
- *test_is_valid_email_bad()* tests if the email address is invalid.

By navigating to the program/app folder where it is extracted - [BirthdayReminderApp](https://github.com/aurimas13/BirthdayReminderApp#birthday-reminder-app) - one folder before where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held and one can run these test commands:

[//]: # ([comment]: <> &#40;For DocTest run this command in terminal:&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;``` python&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;> python -m doctest -v calculator.py&#41;)

[//]: # ()
[//]: # ([comment]: <> &#40;```&#41;)
1) To check source files for errors in the project folder:
```
>>> pyflakes .
```

2) To check source files for errors in test file: 
```
>>> pyflakes Tests/tests.py
```

3) To check typing for test file:
``` 
>>> python -m pytest Tests/tests.py
```
# Errors

There could be a few errors that are coded:
1) 2nd argument error:
```
>>>  python bdayreminder.py Datasets/data_20.csv versada
Argument passed not an integer
```
2)
# Cron Job

To build cron job in mac terminal run:
``` 
>>> crontab -e
```

The syntax for cronjob when entering terminal could look like this<sup>1,2,3</sup>)
``` 
>>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2
[Optional] >>> 0 6 * * * cd <directory_to_app> && <directory_to_python> bdayreminder.py <data_file_path> 2 >> Public/birthdays.txt
```
<br><sup>1</sup> **<directory_to_app>** - should be the directory where BirthdayReminderApp folder is like /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp </br>
<br><sup>2</sup> **<directory_to_python>** should be where you installed python on your machine like /Users/aurimasnausedas/opt/miniconda3/envs/symmetric/bin/python </br>
<br><sup>3</sup> **<data_file_path>** should be the dataset in the directory of app like in /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp by setting it to Datasets/data_20.csv </br>

Syntax customization for Cron Job can be checked [here](https://crontab.guru/).

# Public

Public folder contains three files: 
- [birthdays.txt](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/birthdays.txt) - the output of a Cron Job after implementing the [Optional] command as given at [Cron Job](#cron-job) field.
- [todolist](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/todolist) - the TO DO List.

[//]: # (- [task.pdf]&#40;https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/task.pdf&#41; - the problem for which this program was implemented.)

# Logo

The logo of the Birthday Reminder Application can be found [here](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Public/Photo/birthdaylogo.png).

# License

The MIT [LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)
