# %% Answer to section 2.1
import numpy as np
from collections import namedtuple
import re
from copy import copy
import logging
import random
import sys
from collections.abc import Iterable
import json
from dataclasses import dataclass, field
from enum import Enum
from functools import partial
import time
import functools
from time import sleep
from datetime import datetime
selected_a = "orange"
selected_b = "apple"

selected = f"Selected fruits: {{{selected_a}, {selected_b}}}"
assert selected == "Selected fruits: {orange, apple}"

# %% Answer to section 2.2
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
assert fruits.split(",") == fruits.split(
    ",", 10) == fruits.rsplit(",") == fruits.rsplit(",", 10)

assert fruits.split(",", 3) == ['apple', 'orange',
                                'pineapple', 'cherry,watermelon']
assert fruits.rsplit(",", 3) == ['apple,orange',
                                 'pineapple', 'cherry', 'watermelon']
# %%
data_to_split = "abc_,abc__,abc,,__abc_,_abc"

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

pattern = r"(\d{3}), (\w+); (.+)\n"
splitted = re.findall(pattern, text_data)
print(splitted)

pattern = r"(?<!\d)(\d{3}), (\w+); (.+)\n"
splitted = re.findall(pattern, text_data)
print(splitted)

# %% Answer to section 3.2
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
tasks.sort(key=lambda x: len(x["desc"]), reverse=True)

# %% Answer to section 3.3

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

# %% Answer to section 3.6
assert ({1, 2, 3} or {4, 5, 6}) == {1, 2, 3}
assert (False or []) == []
assert ("Hello" or "World") == "Hello"

assert ({1, 2, 3} and {4, 5, 6}) == {4, 5, 6}
assert (False and []) == False
assert ("Hello" and "World") == "World"

# %% Answer to section 4.1
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

# %% Answer to section 4.3


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

# %% Answer to section 4.4
data_to_unpack = [1, (2, 3), 4]

a, (b, c), d = data_to_unpack
print(a, b, c, d)

# %% Answer to section 4.5
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

# %% Answer to section 5.2
numbers = [1, 2, 3]
numbers_gen = (x*x for x in numbers)
print(type(numbers_gen))

# %% Answer to section 5.3
numbers = {"one": 1, "two": 2}
for key in numbers.keys():
    print(key)

for value in numbers.values():
    print(value)

for key, value in numbers.items():
    print(f"{key}: {value}")

for key in numbers:
    print(key)

# %% Answer to section 5.4

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

# %% Answer to section 6.1


def set_start_time(time=datetime.today()):
    print(f"Time: {time}")


for _ in range(3):
    set_start_time()
    sleep(1.0)

# %% Answer to section 6.2

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

# %% Answer to section 6.3


def run_computation(numbers: list[int | str]):
    pass

# %% Answer to section 6.4


def example(**kwargs):
    pass


example(a=1, b=2)

example(1, 2)

example(2a=1, 2b=2)

example()

# %% Answer to section 6.5


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


# %% Answer to section 7.1
def add_five(x): return x + 5


print(add_five.__name__)


def add_ten(x):
    return x + 10


print(add_ten.__name__)

# %% Answer to section 7.3


def logging_time_app(app_name):
    def decorator(func):
        @functools.wraps(func)
        def logger(*args, **kwargs):
            """Log the time"""
            print(f"{app_name} --- {func.__name__} starts")
            start_t = time.time()
            value_returned = func(*args, **kwargs)
            end_t = time.time()
            print(
                f"{app_name} *** {func.__name__} ends; used time: {end_t - start_t:.2f} s")
            return value_returned

        return logger

    return decorator


@logging_time_app("Task Tracker")
def example_app():
    pass


example_app()

# %% Answer to section 7.4


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


below_fiften = fibonacci(15)
numbers = list(below_fiften)
print(numbers)

# %% Answer to section 7.5


def run_stats_model(dataset, model, output_path):
    calculated_stats = 123
    return calculated_stats


run_stats_model_a = partial(
    run_stats_model, model="model_a", output_path="project_a/stats/")

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


# %% Answer to section 8.2
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


# %% Asnwer to section 8.4
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title!r}, {self.desc!r}, {self.urgency})"

# %% Answer to section 8.5


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class Supervisor:
    def __init__(self, name, employee_id, subordinates):
        super().__init__(name, employee_id)
        self.subordinates = subordinates


# %% Answer to section 9.1


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


# %% Answer to section 9.2


@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float
    dishes: field(default_factory=list)


# %% Answer to section 9.3
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


# %% Answer to section 9.4
User = namedtuple("User", "first_name last_name age")
user = User("John", "Smith", "39")

print(json.dumps(user))

# %% Answer to section 9.5


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


# %% Answer to section 10.1


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

# %% Answer to section 10.2


class Task:
    def __init__(self, title):
        self.title = title


task = Task("Homework")


def get_detail(obj):
    print(sys.getrefcount(obj))


get_detail(task)

# %% Answer to section 10.3


class Task:
    def __init__(self, title, desc, tags=None):
        self.title = title
        self.desc = desc
        self.tags = [] if tags is None else tags

    def __copy__(self):
        new_title = f"Copied: {self.title}"
        new_desc = self.desc
        new_tags = self.tags.copy()
        new_task = self.__class__(new_title, new_desc, new_tags)
        return new_task


task = Task("Homework", "Math and physics", ["school", "urgent"])
new_task = copy(task)
print(new_task.__dict__)

task.tags.append("red")
print(task.tags)

print(new_task.tags)

# %% Answer to section 10.4
whether = "sunny"
if random.randint(1, 100) % 2:
    whether = "cloudy"
else:
    whether = "rainy"

print(whether)

# %% Answer to section 10.5


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


# %%  section 12.2

logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

logger.info("It's an info message.")
logger.warning("It's a warning message.")


# %%
# section 13.1
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
