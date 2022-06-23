# Birthday Reminder App

This is a Birthday Reminder Application that contains **2** *visible* **modules** ([bdayreminder.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/bdayreminder.py)) involves the necessary functionalities while the package also includes tests ([tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py)). Please refer to [Requirements](#requirements) for importing some libraries, packages and modules before looking at the [Usage](#usage) of the app.

# Table of contents

- [Birthday Reminder App](#birthday-reminder-app)
- [Table of contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
- [Tests](#tests)
- [Cron Job](#cron-job)
- [License](#license)

# Requirements
[(Back to top)](#table-of-contents)

**Python 3.9.12** is required to properly execute package's modules, imported libraries and defined functions. Imports of several libraries like dotnet, csv, pytest and typing to name a few are also needed.

# Usage
[(Back to top)](#table-of-contents)

After requirements are met, the app package is set at your MAC or PC and terminal is run you have four options (FYI module takes two arguments):
1) To allow yourself to run validation or check & send - the  second argument has to be **0**: 
```
>>> bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19

>>> bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv 0
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```
2) To run validation or check & send another way - the second argument has to be any **other number** or a **string**:

```
>>> python bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv 3
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> 3
Please choose either 1 or 2
>>> 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19 

>>> python bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv versada
Choose 1 to validate if input data file is correct or 2 to check for upcoming birthdays and send respective emails
>>> versada
Please choose either 1 or 2
>>> 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```

3) To validate birthday persons data file for errors set the second argument to be **1** like this:

```
>>> python bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv 1
ERROR: Invalid email for Laura Dreyfuss at row 6 
ERROR: Empty name field is for email TheoGermaine@goal.com at row 7 
ERROR: Invalid date for Anna Higgins at row 11. Date given is 02-30 
ERROR: Date is in the future for Tom Brady at row 12. Date given is 2075-10-22 
ERROR: Invalid email for Ching Yeung Michael Tam at row 19
``` 
4) To check birtdhay persons data file and send emails set the second argument to be **1** like this:

```
>>> python bdayreminder.py ~/BirthdayReminderApp/Datasets/data_20.csv 2
Kai Yuen Leung will have birthday in a week.
Patrick Kienzle will have birthday in a week.
Emails sent successfully.
```

# Functions
[(Back to top)](#table-of-contents)

def birthday_file(file_path):

def checkBirthdaysInAWeek(input_file, send_emails=False) -> None:

def birthdate_in_7_days() -> str:

def try_parsing_date(date) -> Union[Any, Any]:

def is_valid_input(fmt, item, idx, to_print) -> bool:

def multiple_email_sends(birthday_individuals, to_send) -> None:

# Tests
[(Back to top)](#table-of-contents)

First navigate to where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held or to the folder where the [BirthdayReminderApp](https://github.com/aurimas13/BirthdayReminderApp#birthday-reminder-app) program is extracted.

[comment]: <> (For DocTest run this command in terminal:)

[comment]: <> (``` python)

[comment]: <> (> python -m doctest -v calculator.py)

[comment]: <> (```)
To check source files for errors in the project folder run:
``` python
> pyflakes .
```

While to check source files for errors in test file run: 
``` python
> pyflakes tests.py
```

For typing of test file run:
``` python
> python -m pytest tests.py
``` 

# Cron Job
[(Back to top)](#table-of-contents)

To build cron job in mac terminal run:
``` python
> crontab -e
```

The syntax for cronjob when entering terminal could look like this (cd to the categories on MAC where BirthdayReminderApp folder is & where Python is installed)
``` python
> 0 6 * * * cd ~/BirthdayReminderApp/ && ~/python main.py ~/BirthdayReminderApp/Datasets/data_50.csv 2
[Optional] > 0 6 * * * cd ~/BirthdayReminderApp/ && ~/python main.py ~/BirthdayReminderApp/Datasets/data_50.csv 2 >> Public/birthdays.txt
```

Syntax customization for Cron Job can be checked [here](https://crontab.guru/).
# License
[(Back to top)](#table-of-contents)


[LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)


