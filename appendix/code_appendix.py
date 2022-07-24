#%% Answer to section 2.1
selected_a = "orange"
selected_b = "apple"

selected = f"Selected fruits: {{{selected_a}, {selected_b}}}"
assert selected == "Selected fruits: {orange, apple}"

#%% Answer to section 2.2
x = input("What's today's temperature in your area?")
x_num = float(x)
if x_num < 10:
    x_output = f"You entered {x_num:.1f} degrees. It's cold!"
elif 10 <= x_num < 25:
    x_output = f"You entered {x_num:.1f} degrees. It's cool!"
else:
    x_output = f"You entered {x_num:.1f} degrees. It's hot!"

print(x_output)


x = input("What's today's temperature in your area?")
x_num = float(x)
if x_num < 10:
    x_whether = "cold"
elif 10 <= x_num < 25:
    x_whether = "cool"
else:
    x_whether = "hot"

x_output = f"You entered {x_num:.1f} degrees. It's {x_whether}!"
print(x_output)
# %% Answer to section 2.3
fruits = "apple,orange,pineapple,cherry,watermelon"
assert fruits.split(",") == fruits.split(",", 10) == fruits.rsplit(",") == fruits.rsplit(",", 10)

assert fruits.split(",", 3) == ['apple', 'orange', 'pineapple', 'cherry,watermelon']
assert fruits.rsplit(",", 3) == ['apple,orange', 'pineapple', 'cherry', 'watermelon']
# %%
data_to_split = "abc_,abc__,abc,,__abc_,_abc"

import re
from typing import Type, final
pattern = r"[,_]+"
splitted = re.split(pattern, data_to_split)
print(splitted)
# output: ['abc', 'abc', 'abc', 'abc', 'abc']

# %%
text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""

import re
pattern = r"(\d{3}), (\w+); (.+)\n"
splitted = re.findall(pattern, text_data)
print(splitted)

pattern = r"(?<!\d)(\d{3}), (\w+); (.+)\n"
splitted = re.findall(pattern, text_data)
print(splitted)

#%% Answer to section 3.2
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

def using_by_desc_len(task):
    return len(task["desc"])

tasks.sort(key=using_by_desc_len, reverse=True)
print(tasks)

# using a lambda function
tasks.sort(key=lambda x:len(x["desc"]), reverse=True)

#%% Answer to section 3.3
from collections import namedtuple

Task = namedtuple("Task", "title desc urgency")
task = Task(title='Laundry', desc='Wash clothes', urgency=3)

task.urgency = 4
# the above line of code results in AttributeError

task._replace(urgency=4)
print(task)
# %% Answer to section 3.4
numbers = {"one": 1, "two": 2, "three": 3}
numbers_key = numbers.keys()
id_key = id(numbers_key)
print(id_key)

numbers["four"] = 4
print(numbers_key)
print(id_key)
# %% Answer to section 3.5
assert hash(1) == hash(1.0) == 1

numbers = {1: "one", 1.0: "one point one"}
print(numbers)

#%% Answer to section 3.6
assert ({1, 2, 3} or {4, 5, 6}) == {1, 2, 3}
assert (False or []) == []
assert ("Hello" or "World") == "Hello"

assert ({1, 2, 3} and {4, 5, 6}) == {4, 5, 6}
assert (False and []) == False
assert ("Hello" and "World") == "World"

#%% Answer to section 4.1
num_list = [1, 2, 3, 4]
num_tuple = (1, 2, 3, 4)
num_str = "1234"

print(num_list[:2])
print(num_tuple[:2])
print(num_str[:2])

num_range = range(1, 5)
print(num_range[:2])
# %% Answer to section 4.2
revenue_by_month = [95, 100, 80, 93, 92, 110, 102, 88, 96, 98, 115, 120]
assert revenue_by_month[-2] == revenue_by_month[len(revenue_by_month) - 2]

#%% Answer to section 4.3
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def __eq__(self, __o: object):
        return self.__dict__ == __o.__dict__


tasks = [
    Task("Laundry", 3),
    Task("Museum", 4),
    Task("Homework", 5),
    Task("Ticket", 2)
]

task_to_search = Task("Homework", 5)
print(tasks.index(task_to_search))

#%% Answer to section 4.4
data_to_unpack = [1, (2, 3), 4]

a, (b, c), d = data_to_unpack
print(a, b, c, d)

#%% Answer to section 4.5
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(numbers * 3)

numbers_multipled = []
for number_list in numbers:
    embedded_list = []
    for number in number_list:
        number_multiplied = number * 3
        embedded_list.append(number_multiplied)
    numbers_multipled.append(embedded_list)

print(numbers_multipled)

numbers_multiplied2 = [x*3 for number_list in numbers for x in number_list]
assert number_multiplied == number_multiplied

import numpy as np
numbers_array = np.array(numbers)
print(numbers_array * 3)
# %% Answer to section 5.1
numbers_int = [1, 2, 3]
numbers_word = ("one", "two", "three")
letters = "abc"
for item in zip(numbers_int, numbers_word, letters):
    print(item)


numbers_fewer = [1, 2]
numbers_more = [3, 4, 5, 6]
for item in zip(numbers_fewer, numbers_more):
    print(item)

#%% Answer to section 5.2
numbers = [1, 2, 3]
numbers_gen = (x*x for x in numbers)
print(type(numbers_gen))

#%% Answer to section 5.3
numbers = {"one": 1, "two": 2}
for key in numbers.keys():
    print(key)

for value in numbers.values():
    print(value)

for key, value in numbers.items():
    print(f"{key}: {value}")

for key in numbers:
    print(key)

#%% Answer to section 5.4
from collections import namedtuple

Task = namedtuple("Task", "title, description, urgency")

tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Homework", "Physics and math", 5),
    Task("Floor", "Mop the floor", 3),
    Task("Internet", "Upgrade plan", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4),
    Task("Utility", "Pay bills", 5)
]

first_urgent_task1 = None

for task in tasks:
    if task.urgency == 5:
        first_urgent_task1 = task
        break

print(first_urgent_task1)


for task in tasks:
    if task.urgency > 5:
        first_urgent_task2 = task
        break

print(first_urgent_task2)

#%% Answer to section 6.1
from datetime import datetime
from time import sleep

def set_start_time(time=datetime.today()):
    print(f"Time: {time}")

for _ in range(3):
    set_start_time()
    sleep(1.0)

# %% Answer to section 6.2
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["latitude", "longitude"])

def locate_me():
    # look up the user's current location
    return coordinate0

def locate_home():
    # look up the user's home location
    return coordinate1


def locate_work():
    # look up the user's work location
    return coordinate2
 
#%% Answer to section 6.3
def run_computation(numbers: list[int | str]):
    pass

#%% Answer to section 6.4
def example(**kwargs):
    pass

example(a=1, b=2)

example(1, 2)

example(2a=1, 2b=2)

example()

#%% Answer to section 6.5
def quotient(dividend, divisor, taking_int=False):
    """
    Calculate the product of two numbers with a base factor.

    Args:
      dividend: int | float, the dividend in the division
      divisor: int | float, the divisor in the division
      taking_int: bool, whether only taking the integer part of the quotient;
        default: False, which calculates the precise quotient of the two numbers

    Returns: 
      float | int, the quotient of the dividend and divisor
    
    Raises:
      ZeroDivisionError, when the divisor is 0
    """
    
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    result = dividend / divisor
    if taking_int:
        result = int(result)
    return result

#%% Answer to section 7.1
add_five = lambda x: x + 5
print(add_five.__name__)

def add_ten(x):
    return x + 10
print(add_ten.__name__)

#%% Answer to section 7.3
import functools
import time

def logging_time_app(app_name):
    def decorator(func):
        @functools.wraps(func)
        def logger(*args, **kwargs):
            """Log the time"""
            print(f"{app_name} --- {func.__name__} starts")
            start_t = time.time()
            value_returned = func(*args, **kwargs)
            end_t = time.time()
            print(f"{app_name} *** {func.__name__} ends; used time: {end_t - start_t:.2f} s")
            return value_returned

        return logger

    return decorator

@logging_time_app("Task Tracker")
def example_app():
    pass

example_app()

#%% Answer to section 7.4
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

below_fiften = fibonacci(15)
numbers = list(below_fiften)
print(numbers)

#%% Answer to section 7.5
from functools import partial

def run_stats_model(dataset, model, output_path):
    calculated_stats = 123
    return calculated_stats

run_stats_model_a = partial(run_stats_model, model="model_a", output_path="project_a/stats/")

print(dir(run_stats_model_a))

print(run_stats_model_a.func)

print(run_stats_model_a.args)

print(run_stats_model_a.keywords)
# %% Answer to section 8.1
class Task:
    def __init__(self, title, desc, urgency, tags=None):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        if tags is None:
            self.tags = []
        else:
            self.tags = tags

class Task:
    def __init__(self, title, desc, urgency, tags=None):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.tags = [] if tags is None else tags


#%% Answer to section 8.2
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    @classmethod
    def task_from_tuple(cls, data):
        title, desc, urgency = data
        return cls(title, desc, urgency)

# %% Asnwer to section 8.3
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self._urgency = urgency

    @property
    def urgency(self):
        return self._urgency

    @urgency.setter
    def urgency(self, value):
        if value in range(1, 6):
            self._urgency = value
        else:
            raise ValueError("Can't set a value outside of 1 - 5")


#%% Asnwer to section 8.4
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title!r}, {self.desc!r}, {self.urgency})"

#%% Answer to section 8.5
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Supervisor:
    def __init__(self, name, employee_id, subordinates):
        super().__init__(name, employee_id)
        self.subordinates = subordinates

#%% Answer to section 9.1
from enum import Enum

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def __str__(self):
        return self.name.lower()

    def move_to(self, distance: float):
        if self in self.__class__:
            message = f"Go to the {self} for {distance} miles"
        else:
            message = "Wrong input for direction"
        print(message)

#%% Answer to section 9.2
from dataclasses import dataclass, field

@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float
    dishes: field(default_factory=list)


#%% Answer to section 9.3
class Account:
    def __init__(self, student_id):
        self.student_id = student_id
        # query the database to get additional information using student_id
        self.account_number = self._get_account_number_from_db()
        self.balance = self._get_balance_from_db()

    def _get_account_number_from_db(self):
        # query database to locate the account number using student_id
        account_number = 123456
        return account_number

    def _get_balance_from_db(self):
        # query database to get the balance for the account number
        balance = 100.00
        return balance


class Demographics:
    def __init__(self, student_id):
        self.student_id = student_id
        # query the database to get additional information
        age, gender, race = self._get_demographics_from_db()
        self.age = age
        self.gender = gender
        self.race = race

    def _get_demographics_from_db(self):
        # query database to get the demographics using student_id
        birthday = "08/14/2010"
        age = self._calculated_age(birthday)
        gender = "Female"
        race = "Black"
        return age, gender, race

    @staticmethod
    def _calculated_age(birthday):
        # get today's date and calculate the difference from birthday
        age = 12
        return age


#%% Answer to section 9.4
from collections import namedtuple
User = namedtuple("User", "first_name last_name age")
user = User("John", "Smith", "39")

import json
print(json.dumps(user))

#%% Answer to section 9.5
class ClientV0:
    def __init__(self, first_name, last_name, middle_initial='-'):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.initials = first_name[0] + middle_initial + last_name[0]


class ClientV1:
    def __init__(self, first_name, last_name, middle_initial='-'):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial

    def initials(self):
        return self.first_name[0] + self.middle_initial + self.last_name[0]

class ClientV2:
    def __init__(self, first_name, last_name, middle_initial='-'):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial

    @property
    def initials(self):
        return self.first_name[0] + self.middle_initial + self.last_name[0]

#%% Answer to section 10.1
from collections.abc import Iterable
def is_iterable(obj):
    if isinstance(obj, Iterable):
        outcome = "is an iterable"
    else:
        outcome = "is not an iterable"
    print(type(obj), outcome)

is_iterable([1, 2, 3])
is_iterable((404, "Data"))
is_iterable("abc")
is_iterable(456)

#%% Answer to section 10.2
import sys

class Task:
    def __init__(self, title):
        self.title = title

task = Task("Homework")
def get_detail(obj):
    print(sys.getrefcount(obj))

get_detail(task)

#%% Answer to section 10.3
class Task:
    def __init__(self, title, desc, tags = None):
        self.title = title
        self.desc = desc
        self.tags = [] if tags is None else tags

    def __copy__(self):
        new_title = f"Copied: {self.title}"
        new_desc = self.desc
        new_tags = self.tags.copy()
        new_task = self.__class__(new_title, new_desc, new_tags)
        return new_task

from copy import copy
task = Task("Homework", "Math and physics", ["school", "urgent"])
new_task = copy(task)
print(new_task.__dict__)

task.tags.append("red")
print(task.tags)

print(new_task.tags)

#%% Answer to section 10.4
import random
whether = "sunny"
if random.randint(1, 100) % 2:
    whether = "cloudy"
else:
    whether = "rainy"

print(whether)

#%% Answer to section 10.5
import time
import functools

class TimeLogger:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger

    def __call__(self, *args, **kwargs):
        return self._logger(*args, **kwargs)

@TimeLogger
def calculate_sum(n):
    return sum(range(n))


print(calculate_sum.__name__)


#%% Answer to section 11.1

list_data = [
    '1001,Homework,5', 
    '1002,Laundry,3', 
    '1003,Grocery,4'
]

updated_list_data = [f"{x}\n" for x in list_data]


with open("tasks_list_write.txt", "w") as file:
    file.writelines(updated_list_data)

with open("tasks_list_write.txt") as file:
    print(file.read())


#%% Answer to section 11.2
tasks = [
    ['1001', 'Homework', '5'],
    ['1002', 'Laundry', '3'],
    ['1003', 'Grocery', '4']
]

import csv

with open("tasks_writer.txt", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(tasks)

#%% Answer to section 11.3

import os

class MaliciousTask:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def __reduce__(self):
        print("__reduce__ is called")
        return os.system, ('rm hacking.txt',)

#%% Answer to section 11.4
from pathlib import Path
import shutil

shutil.rmtree("subjects")    

subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)
    
    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        if not target_path.exists():
            _ = shutil.copy(subject_file, target_path)
            print(f"Copying {filename} to {target_path}") 
        else:
            print(f"{filename} already exists at {target_path}")


#%% Answer to section 11.5
from pathlib import Path
import time

def select_recent_files_24h(directory):
    dir_path = Path(directory)
    current_time = time.time()
    time_cutoff = current_time - 24 * 3600
    good_files = []
    for file_path in dir_path.glob("*"):
        file_time = file_path.stat().st_birthtime
        if time_cutoff <= file_time <= current_time:
            good_files.append(file_path)

    return good_files

#%% Answer to section 12.1
import logging

logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    file_handler = logging.FileHandler("taskier.log")
    logger.addHandler(file_handler)

# remove all handlers
print(logger.handlers)
logger.handlers.clear()
print(logger.handlers)

#%%  Answer to section 12.2
import logging

logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

logger.info("It's an info message.")
logger.warning("It's a warning message.")

#%% Answer to section 12.3
urgency = int("3#")

#%% Asnwer to section 12.4
from collections import namedtuple
Task = namedtuple("Task", ["title", "urgency"])

def process_task_challenge(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        task = Task(title, urgency)
        return task
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    finally:
        print(f"Done processing text: {text}")
        return "finally"

processed = process_task_challenge("Laundry,3")
print(processed)

#%% Answer to section 12.5
class Task:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("Please instantiate the Task using string as its title")


def create_task(task_title):  
    try:
        print(f"Trying to process {task_title}")
        task = Task(task_title)
    except TypeError as e:
        print(f"Couldn't create the task, error: {e}")
    else:
        print(f"Created task: {task}")
    finally:
        print(f"Done processing {task_title}")


create_task(100)
create_task("Laundry")



#%%
# Answer to Section 13.1
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def _report(self):
        print("report")
        report = "Urgency: " + self.urgency

    def _send_report(self):
        print("send report")
        self._report()

    def _update_db(self):
        # update the record in the database
        print("update the database")
        self._send_report()

        
    def update_urgency(self, urgency):
        self.urgency = urgency
        self._update_db()

task = Task("Laundry", 3)
task.update_urgency(4)

#%% Answer to section 13.2
# No Python code, see the answer in the Appendix F

#%% Answer to section 13.3
# You need to place them in a separate file and test it using the command line tool as shown in section 13.3
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

def create_task_from_tuple(task_tuple):
    title, urgency = task_tuple
    task = Task(title, urgency)
    return task

import unittest

class TestTaskCreation(unittest.TestCase):
    def setUp(self):
        task_to_compare = Task("Laundry", 3)
        self.task_dict = task_to_compare.__dict__

    def test_create_task_from_tuple(self):
        task_tuple = ("Laundry", 3)
        created_task = create_task_from_tuple(task_tuple)
        self.assertEqual(created_task.__dict__, self.task_dict)


#%% Answer to section 13.4
# Save the following class in the task_class.py
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def formatted_display(self):
        displayed_text = f"{self.title} ({self.urgency})"
        raise TypeError("This is a TypeError")
        # the next return statement will be skipped due to raising an exception
        return displayed_text

#%% Answer to section 14.2
# the following function is taken from the Task class, expects it not to work by itself
def delete_from_db(self):
        """Delete the record from the database
        """
        if app_db == TaskierDBOption.DB_CSV.value:
            with open(app_db, "r+") as file:
                lines = file.readlines()
                found_record = False
                for line in lines:
                    if line.startswith(self.task_id):
                        found_record = True
                        lines.remove(line)
                        break
                if not found_record:
                    raise Exception("Record not found error.")
                else:
                    file.seek(0)
                    file.truncate()
                    file.writelines(lines)

#%% Answer to section 14.3
import functools
import time

def logging_time_wraps(func):
    @functools.wraps(func)
    def logger(*args, **kwargs):
        """Log the time"""
        print(f"--- {func.__name__} starts")
        start_t = time.time()
        value_returned = func(*args, **kwargs)
        end_t = time.time()
        print(f"*** {func.__name__} ends; used time: {end_t - start_t:.10f} s")
        return value_returned

    return logger

#%% Answer to section 14.4
numbers = {0: "zero", 1: "one", 2: "two"}
assert list(numbers) == list(numbers.keys())
