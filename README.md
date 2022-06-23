# Birthday Reminder App

This is a Birthday Remidner App that contains **2** *visible* **modules** ([main.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/main.py) & [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py)) and *7 hidden modules* that were used for experimentation.

The program validates the persons birthday data file (**validation**) and checks whether a single person has a birthday in a week by sending reminders to the rest of the group (**check & send**). 

The main Python file ([main.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/main.py)) involves the necessary functionalities while the package also includes tests ([tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py)). \\

Please refer to [(Installation)](#installation) and [(Requirements)](#requirements) before looking into the [(examples)](#usage).

# Table of contents

- [Birthday Reminder App](#birthday-reminder-app)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Tests](#tests)
- [Cron Job](#cron-job)
- [License](#license)
 
# Installation
[(Back to top)](#table-of-contents)

To run the package you'll have to first download and install it by running this command on colab, jupyter notebook, terminal:
``` python
> pip install git+git://github.com/aurimas13/calculator
```
When it is downloaded navigate to python shell. When there import the module by:
``` python
>>> from calculator.calculator import Calculator
```
or 
``` python
>>> from calculator.calculator import *
```

# Requirements
[(Back to top)](#table-of-contents)

Python 3.8.5 is required to run package's modules. Imports of pytest, math and typing are also needed.

# Usage
[(Back to top)](#table-of-contents)

After installation is done the you'll have to instantiate a Calculator class and play with it by running methods:
```python
>>> calc = Calculator()
>>> calc.add(10)
10
>>> calc.subtract(5)
5
>>> calc.multiply(50)
250
>>> calc.divide(2)
125.0
calc.divide(4.5)
27.7778
>>> calc.multiply(4.5)
125.0001
>>> calc.subtract(25)
100.0001
>>> calc.subtract(2)
98.0001
>>> calc.add(2)
100.0001
>>> calc.root(2)
10.000004999998751
>>> calc.reset()
0
>>> calc.set_memory(6)
>>> calc.get_memory()
6
```
# Tests
[(Back to top)](#table-of-contents)

First navigate to where [tests.py](https://github.com/aurimas13/BirthdayReminderApp/blob/main/Tests/tests.py) is held or to the folder where the program is extracted.

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
[Birthday Reminder App](#birthday-reminder-app)


[LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)


