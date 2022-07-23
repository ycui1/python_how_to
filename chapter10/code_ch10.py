#####################################################################################
#
# 10.1	How do I inspect object's type to improve code flexibility?
#
#####################################################################################
#%%
def filter_tasks(tasks, by_urgency):
    filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

#%%
def filter_tasks(tasks, by_urgency):
    filtered = [x for x in tasks if x.urgency in by_urgency]
    return filtered


#%%
print(type(4))
# output: <class 'int'>

print(type([4, 5]))
# output: <class 'list'>

#%%
assert (type(4) is int)

assert (type([4, 5]) is list)


#%%
def filter_tasks(tasks, by_urgency):
    if type(by_urgency) is list:
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

#%%
assert isinstance(4, int)

assert isinstance([4, 5], list)

#%%
passed_arg0 = [4, 5]
passed_arg1 = (4, 5)

assert isinstance(passed_arg0, (list, tuple))
assert isinstance(passed_arg1, (list, tuple))

#%%
assert isinstance([4, 5], list) or isinstance([4, 5], tuple)

#%%
def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, list):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

#%%
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
# output: [False, True, True, True]

#%%
def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, (list, tuple)):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

#%%
from collections.abc import Collection

def filter_tasks(tasks, by_urgency):
    if isinstance(by_urgency, Collection):
        filtered = [x for x in tasks if x.urgency in by_urgency]
    else:
        filtered = [x for x in tasks if x.urgency == by_urgency]
    return filtered

#####################################################################################
#
# 10.2	What's the life cycle of instance objects?
#
#####################################################################################
#%%
class Task:
    def __new__(cls, *args):
        new_task = object.__new__(cls)
        print(f"__new__ is called, creating an instance at {id(new_task)}")
        return new_task

    def __init__(self, title):
        self.title = title
        print(f"__init__ is called, initializing an instance at {id(self)}")

#%%
task = Task("Laundry")

print("task memory address:", id(task))
# output: task memory address: 140557771534976

#%%
title_output = f"Title: {task.title}"

#%%
print(globals())

#%%
assert Task is globals()["Task"]

assert task is globals()["task"]


#%%
import sys

task = Task("Laundry")

assert sys.getrefcount(task) == 2


#%%
work = {"to_do": task}
assert sys.getrefcount(task) == 3

tasks = [task]
assert sys.getrefcount(task) == 4


#%%
del tasks
assert sys.getrefcount(task) == 3

#%%
work["to_do"] = "nothing"
assert sys.getrefcount(task) == 2

#%%
class Task:
    def __init__(self, title):
        print(f"__init__ is called, initializing an instance at {id(self)}")
        self.title = title

    def __del__(self):
        print(f"__del__ is called, destructing an instance at {id(self)}")


#%%
task = Task("Homework")
# output: __init__ is called, initializing an instance at 140557504542416

assert "task" in globals()

#%%
del task
# output: __del__ is called, destructing an instance at 140557504542416

assert "task" not in globals()

#%%
# expect errors
title_output = f"Title: {task.title}"
# ERROR: NameError: name 'task' is not defined. Did you mean: 'Task'?


#####################################################################################
#
# 10.3	How do I copy an object?
#
#####################################################################################
#%%
class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r})"

    def save_data(self):
        # update the database
        pass

#%%
task_dict = task.__dict__

task_dict_copied = task_dict.copy()

print(task_dict_copied)
# output: {'title': 'Homework', 'desc': 'Math and physics'}

#%%
from copy import copy

task_copied = copy(task)

print(task_copied)
# output: Task('Homework', 'Math and physics')


#%%
class Task:
    def __init__(self, title, desc, tags = None):
        self.title = title
        self.desc = desc
        self.tags = [] if tags is None else tags    #A

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.tags})"

    def save_data(self):
        pass

#%%
task = Task("Homework", "Math and physics", ["school", "urgent"])

task_copied = copy(task)

print(task_copied)
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])

#%%
task_copied.tags.append("red")

print(task_copied)
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])

#%%
print(task)
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])

#%%
assert task.tags is task_copied.tags

assert id(task.tags) == id(task_copied.tags)

#%%
from copy import deepcopy

task = Task("Homework", "Math and physics", ["school", "urgent"])

task_deepcopied = deepcopy(task)

print(task_deepcopied)
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])

#%%
task_deepcopied.tags.append("red")

print(task_deepcopied)
# output: Task('Homework', 'Math and physics', ['school', 'urgent', 'red'])

print(task)
# output: Task('Homework', 'Math and physics', ['school', 'urgent'])

#####################################################################################
#
# 10.4  How do I access and change a variable in a different scope?
#
#####################################################################################
#%%

#%%
db_filename = "N/A"

def set_database(db_name):
    db_filename = db_name

set_database("tasks.sqlite")

print(db_filename)
# output: "N/A"

#%%
db_filename = "N/A"

def set_database(db_name):
    db_filename = db_name
    print(list(locals()))

#%%
print(list(globals()))

#%%
set_database("tasks.sqlite")
# output: ['db_name', 'db_filename']

#%%
db_filename = "N/A"

def set_database(db_name):
    global db_filename
    db_filename = db_name
    print(list(locals()))

set_database("tasks.sqlite")
# output: ['db_name']

print(db_filename)
# output: tasks.sqlite

#%%
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

#####################################################################################
#
# 10.5	What's callability and what 're its implications?
#
#####################################################################################

#%%
def doubler(x):
    return 2 * x

assert callable(doubler)

#%%
def do_something():
    pass

print(do_something)
# output: <function do_something at 0x7fe8180f30a0>

print(sum)
# output: <built-in function sum>

#%%
print(map)
# output: <class 'map'>

#%%
print(map(int, ["1", "2.0", "3"]))
# output: <map object at 0x7fe8180df700>

#%%
# expect errors
cards = [10, 1, "J", "A"]

print(sorted(cards))
# ERROR: TypeError: '<' not supported between instances of 'str' and 'int'

print(sorted(cards, key=str))
# output: [1, 10, 'A', 'J']

#%%
class PokerOrder(int):
    def __new__(cls, x):
        numbers_mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        casted_number = numbers_mapping.get(x, x)
        return super().__new__(PokerOrder, casted_number)

#%%
print(sorted(cards, key=PokerOrder))
# output: [1, 10, 'J', 'A']

#%%
import time

def logging_time(func):
    def logger(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")
        return result

    return logger

#%%
import time

class TimeLogger:
    def __init__(self, func):
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger

    def __call__(self, *args, **kwargs):
        return self._logger(*args, **kwargs)

#%%
@TimeLogger
def calculate_sum(n):
    return sum(range(n))

result = calculate_sum(100_000)
# output: Calling calculate_sum: 0.00181

#%%
print(calculate_sum)

# output: <__main__.TimeLogger object at 0x7fe8180de710>