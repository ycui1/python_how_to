num_dict = dict(one=1, two=2)

def is_iterable(obj):
    try:
        _ = iter(obj)
    except TypeError:
        print(type(obj), "is not an iterable")
    else:
        print(type(obj), "is an iterable")

is_iterable(5)
is_iterable([1, 2, 3])

integers_list = list(range(10))
print(integers_list)

integers_tuple = tuple(integers_list)
print(integers_tuple)

dict_items = [("zero", 0), ("one", 1), ("two", 2)]
integers_dict = dict(dict_items)
print(integers_dict)

even_numbers = (-2, 4, 0, 2, 4, 2)
unique_evens = set(even_numbers)
print(unique_evens)


words = ["zero", "one", "two"]
numbers = [0, 1, 2]
zipped_dict = dict(zip(words, numbers))
print(zipped_dict)

numbers_str = ["1.23", "4.56", "7.89"]
numbers_float = list(map(float, numbers_str))
print(numbers_float)

from collections import namedtuple

Task = namedtuple("Task", "title, description, urgency")
tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]

task_titles = []
for task in tasks:
    task_titles.append(task.title)
    
print(task_titles)

titles = [task.title for task in tasks]
print(titles)

title_dict0 = {}
for task in tasks:
    title_dict0[task.title] = task.description
    
title_dict1 = {task.title: task.description for task in tasks}

assert title_dict0 == title_dict1

title_set0 = set()
for task in tasks:
    title_set0.add(task.title)

title_set1 = {task.title for task in tasks}

assert title_set0 == title_set1

numbers = [-3, -2, -1, 0, 1, 2, 3]
squares = {x*x for x in numbers}
print(squares)

filtered_titles0 = []
for task in tasks:
    if task.urgency > 3:
        filtered_titles0.append(task.title)
        
print(filtered_titles0)

filtered_titles1 = [task.title for task in tasks if task.urgency > 3]
assert filtered_titles0 == filtered_titles1

flattened_items0 = []
for task in tasks:
    for item in task:
        flattened_items0.append(item)
        
print(flattened_items0)

flattened_items1 = [item for task in tasks for item in task]
assert flattened_items0 == flattened_items1


styles = ['long-sleeve', 'v-neck']
colors = ['white', 'black']
sizes = ['L', 'S']

options = [' '.join([x, y, z]) for x in styles for y in colors for z in sizes]

options = []
for x in styles:
    for y in colors:
        for z in sizes:
            option = ' '.join([x, y, z])
            options.append(option)


from collections import namedtuple

Task = namedtuple("Task", "title description urgency")
tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]

for task_i in range(len(tasks)):
    task = tasks[task_i]
    task_counter = task_i + 1
    print(f"Task {task_counter}: {task.title:<10} {task.description:<18} {task.urgency}")
    
for task_i, task in enumerate(tasks, start=1):
    print(f"Task {task_i}: {task.title:<10} {task.description:<18} {task.urgency}")
    
for task_i in range(len(tasks)):
    task = tasks[-(task_i + 1)]
    print(f"Task: {task}")
    
for task in reversed(tasks):
    print(f"Task: {task}")
    
dates = ["May 5, 2022", "May 9, 2022", "May 11, 2022"]
locations = ["School", "Home", "Downtown"]

for task_i in range(len(tasks)):
    task = tasks[task_i]
    date = dates[task_i]
    location = locations[task_i]
    print(f"{task.title}: by {date} at {location}")
    

for task, date, location in zip(tasks, dates, locations):
    print(f"{task.title}: by {date} at {location}")
    
from itertools import zip_longest
list(zip_longest(range(3), range(4), range(5)))

completed_tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Floor", "Mop the floor", 3)
]

all_tasks = tasks + completed_tasks
for task in all_tasks:
    print(task.title)
    
from itertools import chain

for task in chain(tasks, completed_tasks):
    print(task.title)
    
for task in tasks:
    if task.urgency > 3:
        print(task)
        
for task in filter(lambda x: x.urgency > 3, tasks):
    print(task)
    
    
for number in range(5):
    print(f"Number: {number}")
    if number == 2:
        print("Breaking at 2")
        break


number = 0
while True:
    if number == 2:
        print("Breaking at 2")
        break
    else:
        number += 1
        print(f"Number: {number}")
    

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

urgent_tasks = [x for x in tasks if x.urgency == 5]
first_urgent_task0 = urgent_tasks[0]
print(first_urgent_task0)

for task in tasks:
    if task.urgency == 5:
        first_urgent_task1 = task
        break
    
assert first_urgent_task0 == first_urgent_task1

for number in range(5):
    if number < 3:
        continue
    print(f"Number: {number}")
    
    
for task in tasks:
    if task.urgency == 5:
        result0 = task.do_something0()
        result1 = task.do_something1()
        if result0 >= 0 and result1 == "Hello":
            task.do_something2()
            task.do_something3()
            task.do_something4()


for task in tasks:
    if task.urgency < 5:
        continue
    result0 = task.do_something0()
    result1 = task.do_something1()
    if result0 < 0 or result1 != "Hello":
        continue
    task.do_something2()
    task.do_something3()
    task.do_something4()
    
def use_else_in_for(apply_break):
    for number in range(2):
        if apply_break:
            break
        print(number)
    else:
        print("Running the else statement")
    print("Outside the for...else...")

use_else_in_for(False)
use_else_in_for(True)

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

def locate_task(urgency_level):
    for task in tasks:
        if task.urgency == urgency_level:
            working_task = task
            break
    else:
        working_task = None
    print(f"Working Task: {working_task}")

locate_task(1)
locate_task(4)

def complete_tasks_with_break(resting_threshold):
    completed_urgency_levels = 0
    while tasks:
        if completed_urgency_levels > resting_threshold:
            print("Coffee break now!")
            break
        next_task = tasks.pop()
        print(f"Completed: {next_task}")
        completed_urgency_levels += next_task.urgency
    else:
        print("Party! Completed all the tasks.")

tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Homework", "Physics and math", 5),
    Task("Floor", "Mop the floor", 3),
    Task("Internet", "Upgrade plan", 5)
]

complete_tasks_with_break(7)
complete_tasks_with_break(6)
complete_tasks_with_break(5)


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
]    #A

first_urgent_task = None
for count, task in enumerate(tasks, 1):
    print(f"---checking task {count}: {task.title}")
    if (task.urgency == 5) and (first_urgent_task is None):
        first_urgent_task = task

print(f"***first urgent task: {first_urgent_task.title}")


def show_for_else_rule(breaking_number):
    for number in range(2):
        print(f"Iteration: {number}")
        if number == breaking_number:
            print(f"Break: {number}; Skip the else statement")
            break
    else:
        print("Running the else statement")
    print("Outside the for...else...")

show_for_else_rule(1)

show_for_else_rule(3)

