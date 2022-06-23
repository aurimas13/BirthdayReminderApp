# BirthdayReminderApp
# TO UPDATE by 2022/06/24

The repository includes a developed \textbf{Python} program that checks whether a person has a birthday in a week and then sends reminders to the rest of the group. The program involves the necessary functionalities for sending emails, checking for errors and includes tests. \\




#CRON JOB
cron job - 52 20 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/test_data.csv 1 >> Public/output.txt
crontab -e - 10 12 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python  main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/test_data.csv 2 >> Public/output.txt
crontab -e -> 46 12 * * * cd /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/ && /Users/aurimasnausedas/opt/miniconda3/bin/python  main.py /Users/aurimasnausedas/Documents/Python/BirthdayReminderApp/Datasets/data.csv 2 >> Public/birthdays.txt

# Calculator-program

This is a Calculator package that contains **5 modules** ([calculator.py](https://github.com/aurimas13/calculator/blob/main/calculator/calculator.py), [tests.py](https://github.com/aurimas13/calculator/blob/main/test/tests.py), [setup.py](https://github.com/aurimas13/calculator/blob/main/setup.py),[__init__.py](https://github.com/aurimas13/Calculator/blob/main/calculator/__init__.py) for *calulator.py* and [__init__.py](https://github.com/aurimas13/Calculator/blob/main/tests/__init__.py) for *tests.py*), [Dockerfile](https://github.com/aurimas13/calculator/blob/main/Dockerfile), [LICENSE](https://github.com/aurimas13/calculator/blob/main/LICENSE), [.gitignore](https://github.com/aurimas13/calculator/blob/main/.gitignore) and [.dockerignore](https://github.com/aurimas13/calculator/blob/main/.dockerignore). 
The written [calculator.py](https://github.com/aurimas13/calculator/blob/main/calculator/calculator.py) module acts as a normal calculator by adding, subtracting, multiplying, dividing and taking the nth root of a number. This module also contains methods of reseting memory, allocating memory from what you want to start, setting and getting a memory value (not to be confused with *memory allocation* to *stack* and *heap*). Please refer to [(Installation)](#installation) and [(Requirements)](#requirements) before looking into the [(examples)](#usage).

# Table of contents

- [Calculator](#Calculator)
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

# CRON JOB
[(Back to top)](#table-of-contents)

Setup up of [Cron Job](https://github.com/aurimas13/calculator/blob/main/Dockerfile).

To build docker image on terminal run:
``` python
> docker build -t calculatorapp .
```
To enter python prompt through docker:
``` python
> docker run -it calculatorapp python 
```
The commands to run in it are shown in [(Usage)](#usage)

# License
[(Back to top)](#table-of-contents)


[LICENSE](https://github.com/aurimas13/BirthdayReminderApp/blob/main/LICENSE)


