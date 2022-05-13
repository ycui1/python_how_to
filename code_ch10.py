import imp
from numpy import isin


print(type("created"))
# output <class 'str'>

print(type(["created", "completed"]))
# output <class 'list'>

print(type("created") == str)
# output True

print(type(["created", "completed"]) == list)
# output True

def filter_tasks(tasks, by_status):
    if type(by_status) is str:
        filtered = [x for x in tasks if x.status == by_status]
    else:
        filtered = [x for x in tasks if x.status in by_status]
    return filtered

print(isinstance("created", str))
# output True

print(isinstance(["created", "completed"], list))
# output True

print(isinstance("created", (str, int)))

class User:
    pass

class Supervisor(User):
    pass

supervisor = Supervisor()

comparisons = [
    type(supervisor) is User,
    type(supervisor) is Supervisor,
    isinstance(supervisor, User),
    isinstance(supervisor, Supervisor)
]

print(comparisons)

def filter_tasks(tasks, by_status):
    if isinstance(by_status, (list, tuple, set)):
        filtered = [x for x in tasks if x.status in by_status]
    else:
        filtered = [x for x in tasks if x.status == by_status]
    return filtered 

import pandas as pd
numbers = pd.Series([1, 2, 3])
import collections.abc

isinstance(numbers, collections.abc.Collection)

class Task:
    def __new__(cls, *args):
        new_task = object.__new__(cls)
        print(f"__new__ is called, creating an instance at {id(new_task)}")
        return new_task

    def __init__(self, title):
        self.title = title
        print(f"__init__ is called, initializing an instance at {id(self)}")


task = Task("Laundry")

task1 = task

print("task memory address:", id(task))

print(globals())

assert Task is globals()["Task"]
assert task is globals()["task"]



import imp
import sys

task = Task("Laundry")

assert sys.getrefcount(task) == 2

work = {"to_do": task}

assert sys.getrefcount(task) == 3

tasks = [task]

assert sys.getrefcount(task) == 4

del tasks
assert sys.getrefcount(task) == 3

work["to_do"] = "nothing"
assert sys.getrefcount(task) == 2

class Task:
    def __init__(self, title):
        print(f"__init__ is called, initializing an instance at {id(self)}")
        self.title = title

    def __del__(self):
        print(f"__del__ is called, destructing an instance at {id(self)}")


task = Task("Homework")

assert "task" in globals()

del task

assert "task" not in globals()

class Task:
    def __init__(self, title):
        print(f"__init__ is called, initializing an instance at {id(self)}")
        self.title = title

    def __del__(self):
        print(f"__del__ is called, destructing an instance at {id(self)}")


task = Task("Homework")

sys.getrefcount(task)

task1 = task

from copy import copy

class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r})"

    def save_data(self):
        pass

task = Task("Homework", "Math and physics")

task_dict = task.__dict__
task_dict_copied = task_dict.copy()
print(task_dict_copied)

task_copied = copy(task)
print(task_copied)

class Task:
    def __init__(self, title, desc, tags = None):
        self.title = title
        self.desc = desc
        self.tags = [] if tags is None else tags

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.tags})"

    def __copy__(self):
        print("__copy__ is called")

task = Task("Homework", "Math and physics", ["school", "urgent"])
task_copied = copy(task)
print(task_copied)

task_copied.tags.append("red")
print(task_copied)

print(task)

assert task.tags is task_copied.tags

assert id(task.tags) == id(task_copied.tags)

from copy import deepcopy

task = Task("Homework", "Math and physics", ["school", "urgent"])
task_deepcopied = deepcopy(task)
print(task_deepcopied)


task_deepcopied.tags.append("red")
print(task_deepcopied)
print(task)

task.title is task_deepcopied.title

task.title is task_copied.title


db_filename = "N/A"

def set_database(db_name):
    db_filename = db_name

set_database("tasks.sqlite")

print(db_filename)
# output: "N/A"



number = int("5")

def outer_fun(info):
    print(info)
    x = 100
    def inner_fun():
        number_str = f"number: {number}"
        x_str = f"x: {x}"
        print(number_str, x_str)

    return inner_fun

inner = outer_fun("test")

b = int(a)

db_filename = "N/A"

def set_database(db_name):
    global db_filename
    db_filename = db_name
    print(list(locals()))

set_database("tasks.sqlite")

print(db_filename)
# output: "N/A"

def change_text(using_nonlocal: bool):
    text = "N/A"
    def inner_fun0():
        text = "No nonlocal"

    def inner_fun1():
        nonlocal text
        text = "Using nonlocal"
        
    inner_fun1() if using_nonlocal else inner_fun0()
    return text


change_text(using_nonlocal=False)
# output: 'N/A'

change_text(using_nonlocal=True)
# output: 'Using nonlocal'



change_text(using_nonlocal=False)

change_text(using_nonlocal=True)

global_ns = globals()
global_ns

global_ns["new_data"] = 567

class Test:
    available = locals()

Test.available

def do_something():
    pass


def doubler(x):
    return 2 * x

assert callable(doubler)


print(do_something)

print(sum)

print(map)

print(map(int, ["1", "2.0", "3"]))

cards = [10, 1, "J", "A"]
print(sorted(cards))

print(sorted(cards, key=str))

class PokerOrder(int):
    def __new__(cls, x):
        numbers_mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        casted_number = numbers_mapping.get(x, x)
        return super().__new__(PokerOrder, casted_number)


print(sorted(cards, key=PokerOrder))

import time

def logging_time(func):
    def logger(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")
        return result

    return logger


class TimeLogger:
    def __init__(self, func):
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger
        self._tracked_results = {}

    def __call__(self, *args, **kwargs):
        if args in self._tracked_results:
            return self._tracked_results[args]
        return self._logger(*args, **kwargs)

@TimeLogger
def calculate_sum(n):
    return sum(range(n))

result = calculate_sum(100_000)

print(calculate_sum)

class TimeLogger:
    def __init__(self, func):
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger
        self._tracked_results = {}

    def __call__(self, *args, **kwargs):
        if args in self._tracked_results:
            return self._tracked_results[args]
        return self._logger(*args, **kwargs)

@TimeLogger
def calculate_sum(n):
    return sum(range(n))

import functools


import keyword

keyword.kwlist