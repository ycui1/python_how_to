#####################################################################################
#
# 5.1	How do I create common data containers using iterables?
#
#####################################################################################

# %%
from itertools import chain
from collections import namedtuple
id_numbers = [101, 102, 103]
titles = ["Laundry", "Homework", "Soccer"]

desired_output = {101: "Laundry", 102: "Homework", 103: "Soccer"}

# %%
desired_output = {}
for item_i in range(len(id_numbers)):
    desired_output[id_numbers[item_i]] = titles[item_i]
print(desired_output)
# %%
desired_output = {key: value for key, value in zip(id_numbers, titles)}
print(desired_output)

num_dict = dict(one=1, two=2)
num_dict

# %%
tasks = ["task0", "task1", "task2"]

tasks_iterator = iter(tasks)

tasks_iterator
# output: <list_iterator object at 0x000001F232ACEE50>    #A

# %%
next(tasks_iterator)
# output: 'task0'

next(tasks_iterator)
# output: 'task1'

next(tasks_iterator)
# output: 'task2'

next(tasks_iterator)
# ERROR: StopIteration

# %%
for task in tasks:
    print(task)

# %%
iter(5)
# ERROR: TypeError: 'int' object is not iterable

iter([1, 2, 3])
# output: <list_iterator object at 0x000001F232A44700>


#####################################################################################
#
# 5.2	What are list, dictionary, and set comprehensions?
#
#####################################################################################
# %%
numbers = [1, 2, 3, 4]
squares = [x * x for x in numbers]

assert squares == [1, 4, 9, 16]

# %%

Task = namedtuple("Task", "title, description, urgency")  # A

tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]

# %%
task_titles = []
for task in tasks:
    task_titles.append(task.title)

assert task_titles == ['Homework', 'Laundry', 'Museum']

# %%
titles = [task.title for task in tasks]

assert titles == ['Homework', 'Laundry', 'Museum']

# %%
title_dict0 = {}
for task in tasks:
    title_dict0[task.title] = task.description

title_dict1 = {task.title: task.description for task in tasks}

assert title_dict0 == title_dict1
print(f"t0: {title_dict0}")
print('-----------------')
print(f"t1: {title_dict1}")

# %%
title_set0 = set()  # A
for task in tasks:
    title_set0.add(task.title)

title_set1 = {task.title for task in tasks}

assert title_set0 == title_set1 == {'Homework', 'Laundry', 'Museum'}

# %%
numbers = [-3, -2, -1, 0, 1, 2, 3]

squares = {x*x for x in numbers}

assert squares == {0, 9, 4, 1}  # A

# %%
filtered_titles0 = []
for task in tasks:
    if task.urgency > 3:
        filtered_titles0.append(task.title)

assert filtered_titles0 == ['Homework', 'Museum']

# %%
filtered_titles1 = [task.title for task in tasks if task.urgency > 3]

assert filtered_titles0 == filtered_titles1

# %%
flattened_items0 = []
for task in tasks:
    for item in task:
        flattened_items0.append(item)

assert flattened_items0 == ['Homework', 'Physics and math', 5,
                            'Laundry', 'Wash clothes', 3, 'Museum', 'Egypt exhibit', 4]

# %%
flattened_items1 = [item for task in tasks for item in task]

assert flattened_items0 == flattened_items1

# %%
styles = ['long-sleeve', 'v-neck']
colors = ['white', 'black']
sizes = ['L', 'S']

options1 = [' '.join([style, color, size])
            for style in styles for color in colors for size in sizes]

# %%
options2 = []
for style in styles:
    for color in colors:
        for size in sizes:
            option = ' '.join([style, color, size])
            options2.append(option)

assert options1 == options2
#####################################################################################
#
# 5.3	How do I improve for-loop iterations with built-in functions?
#
#####################################################################################
# %%

Task = namedtuple("Task", "title description urgency")
tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]
tasks
# %%
for task_i in range(len(tasks)):
    task = tasks[task_i]
    task_counter = task_i + 1
    print(
        f"Task {task_counter}: {task.title:<10} {task.description:<18} {task.urgency}")

# %%
for task_i, task in enumerate(tasks, start=1):
    print(
        f"Task {task_i}: {task.title:<10} {task.description:<18} {task.urgency}")

# %%
for task_i in range(len(tasks)):
    task = tasks[-(task_i + 1)]
    print(f"Task: {task}")

# %%
for task in reversed(tasks):
    print(f"Task: {task}")

# %%
dates = ["May 5, 2022", "May 9, 2022", "May 11, 2022"]

locations = ["School", "Home", "Downtown"]

# %%
for task_i in range(len(tasks)):
    task = tasks[task_i]
    date = dates[task_i]
    location = locations[task_i]
    print(f"{task.title}: by {date} at {location}")

# %%
for task, date, location in zip(tasks, dates, locations):
    print(f"{task.title:<10}: by {date:^15} at {location:^15}")

# %%
completed_tasks = [
    Task("Toaster", "Clean the toaster", 2),
    Task("Camera", "Export photos", 4),
    Task("Floor", "Mop the floor", 3)
]

# %%
all_tasks = tasks + completed_tasks
for task in all_tasks:
    print(task.title)

# %%

for task in chain(tasks, completed_tasks):
    print(task.title)

# %%
for task in tasks:
    if task.urgency > 3:
        print(task)

# %%
for task in filter(lambda x: x.urgency > 3, tasks):
    print(task)
# %%
tasks = ["task1", "task2", "task3"]
for task in reversed(tasks):
    print(task)


#####################################################################################
#
# 5.4	Using optional statements within for and while loops
#
#####################################################################################
# %%

# %%

# %%
n = 1
while n < 3:
    print(f"n's value: {n}")
    n += 1

print(f"n's value after while loop: {n}")

# %%

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
]  # A

# %%
first_urgent_task0 = None
for counter, task in enumerate(tasks, 1):
    print(f"---checking task {counter}: {task.title}")
    if (task.urgency == 5) and (first_urgent_task0 is None):  # A
        first_urgent_task0 = task
        break

print(f"***first urgent task: {first_urgent_task0}")


# %%
for number in range(5):
    print(f"Number: {number}")
    if number == 2:
        print("Breaking at 2")
        break

# %%
number = 0
while number < 100:
    if number == 2:
        print("Breaking at 2")
        break
    else:
        number += 1
        print(f"Number: {number}")

# %%
first_urgent_task1 = None  # A

for task in tasks:
    if task.urgency == 5:
        first_urgent_task1 = task
        break

assert first_urgent_task0 == first_urgent_task1

# %%
for number in range(5):
    if number < 3:
        continue
    print(f"Number: {number}")

# %%
# Note that these do_something functions are for demostration purposes
for task in tasks:
    if task.urgency > 4:
        result0 = task.do_something0()
        result1 = task.do_something1()
        if (result0 >= 0) and (result1 == "Hello"):
            task.do_something2()
            task.do_something3()
            task.do_something4()

# %%
for task in tasks:
    if task.urgency <= 4:
        continue
    result0 = task.do_something0()
    result1 = task.do_something1()
    if (result0 < 0) or (result1 != "Hello"):
        continue
    task.do_something2()
    task.do_something3()
    task.do_something4()

# %%


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

show_for_else_rule(5)

# %%


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

# %%


def complete_tasks_with_break(resting_threshold):
    completed_urgency_levels = 0
    while tasks:  # A
        if completed_urgency_levels > resting_threshold:
            print("Coffee break now!")
            break
        next_task = tasks.pop()  # B
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
print("--------------")
complete_tasks_with_break(6)
print("--------------")
complete_tasks_with_break(5)

# %%
