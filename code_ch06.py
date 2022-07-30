#####################################################################################
#
# 6.1	How do I set default arguments to make function calls easier?
#
#####################################################################################
# %%
from collections import namedtuple
from statistics import mean, stdev
numbers = [4, 5, 7, 2]

numbers.sort()

assert numbers == [2, 4, 5, 7]

# %%
numbers.sort(reverse=True)

assert numbers == [7, 5, 4, 2]

# %%


class Task:  # A
    def __init__(self, title, description, urgency):
        self.title = title
        self.description = description
        self.urgency = urgency


def complete_task(task):
    task.status = "completed"
    print(f"{task.title}'s status: completed")
    task.name = "tarea de prueba"
    print(f"Nombre de la tarea: {task.name}")


task = Task("Homework", "Physics and math", 5)
complete_task(task)

# %%


def complete_task(task, note):
    task.status = "completed"
    task.note = note
    print(f"{task.title}'s status: completed; note: {note}")


# %%
# note that task1, task2, and task3 are instances of Tasks
# Use case 1
complete_task(task1, "")

# Use case 2
complete_task(task2, "")

# Use case 3
complete_task(task3, "")

# %%


def complete_task(task, note=""):
    task.status = "completed"
    task.note = note
    print(f"{task.title}'s status: completed; note: {note}")


# %%
complete_task(task)

# %%


def complete_task(task, grouped_tasks=[]):
    task.status = "completed"
    grouped_tasks.append(task.title)  # A
    return grouped_tasks


# %%
task0 = Task("Homework", "Physics and math", 5)
task1 = Task("Fishing", "Fishing at the lake", 3)

work_tasks = complete_task(task0)
play_tasks = complete_task(task1)

print("Work Tasks:", work_tasks)
print("Play Tasks:", play_tasks)

# %%
assert work_tasks == play_tasks

assert work_tasks is play_tasks  # A

# %%


def append_task(task, tasks=[]):
    tasks.append(task)
    print(f"Tasks: {tasks}; id: {id(tasks)}")  # A


append_task.__defaults__  # B
# output: ([],)

id(append_task.__defaults__[0])
# output: 4356663616

append_task("Homework")
# output: Tasks: ['Homework']; id: 4356663616

append_task("Laundry")
# output: Tasks: ['Homework', 'Laundry']; id: 4356663616

append_task.__defaults__
# output: (['Homework', 'Laundry'],)

# %%


def complete_task(task, grouped_tasks=None):
    task.status = "completed"
    if grouped_tasks is None:  # A
        grouped_tasks = []
    grouped_tasks.append(task.title)
    return grouped_tasks


complete_task.__defaults__
# output: (None,)

#####################################################################################
#
# 6.2	How do I set and use the return value in function calls?
#
#####################################################################################
# %%
numbers = list(range(5))

sum_numbers = sum(numbers)

print(f"Sum of {numbers} is {sum_numbers}")
# output: Sum of [0, 1, 2, 3, 4] is 10

# %%
primes = [5, 7, 2, 3, 11]

sort_return_value = primes.sort()

print(f"Return value of sort: {sort_return_value}")
# output: Return value of sort: None


# %%
# Expect error for the following code
primes.sort().append(13)

# %%


def append_task(task, grouped_tasks):
    grouped_tasks.append(task)


appended_no_return = append_task("Homework", [])

print(f"Appended: {appended_no_return}")
# output: Appended: None

# %%


def say_hello(person):
    hello = f"Hello, {person}!"
    return hello


greeting = say_hello("Rocky")

# %%


def generate_stats(measures):
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std

# %%


def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean


def calculate_std(measures):
    measure_std = stdev(measures)
    return measure_std

# %%


def process_data(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    measure_mean = mean(measures)
    return formatted_measures, measure_mean


# %%
def format_measures(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    return formatted_measures


def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean


# %%
measures = [5.6, 7.0, 5.7, 5.8, 4.3, 5.2]

measures_stats = generate_stats(measures)

print(type(measures_stats), measures_stats)  # A
# output: <class 'tuple'> (5.6, 0.8786353054595518)

# %%
m_mean, m_std = generate_stats(measures)

print(f"Mean: {m_mean}; SD: {m_std}")
# output: Mean: 5.6; SD: 0.8786353054595518

#####################################################################################
#
# 6.3	How do I use type hints to write understandable functions?
#
#####################################################################################
# %%


def generate_stats(measures):
    pass


# %%
generate_stats({"measure0": 7.9, "measure1": 6.8, "measure2": 7.0})

# %%
number = 1

print(type(number))
# output: <class 'int'>

# %%
number = "one"

print(type(number))
# output: <class 'str'>

# %%
# note that the below is Swift code
var number = 1

number = "one"
error: cannot assign value of type 'String' to type 'Int'

# %%
number: int = 3

name: str = "John"

primes: list = [1, 2, 3]

# %%
numbers: tuple = (1, 2, 3)

numbers = [1, 2, 3]

# %%


def generate_stats(measures: list) -> tuple:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


# %%
help(generate_stats)

# %%


def calculate_product(a: int, b: int, multiplier: int = 1) -> int:
    c = a * b * multiplier
    return c


# %%

Task = namedtuple("Task", "title description urgency")


class User:
    pass  # A


def assign_task(pending_task: Task, user: User):
    pass

# %%


def complete_tasks(tasks: list):
    for task in tasks:
        pass


# %%
complete_tasks(["Laundry", "Museum"])

complete_tasks([Task("Laundry", "Wash clothes", 5),
               Task("Museum", "Egyptian exhibit", 4)])

# %%


def complete_tasks_hinted(tasks: list[Task]):
    for task in tasks:
        pass


# %%


def generate_stats(measures: list[float] | tuple[float, ...]) -> tuple[float, float]:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


#####################################################################################
#
# 6.4	How do I increase function flexibility with *args and **kwargs?
#
#####################################################################################
# %%
word = "Hello"
numbers = [1, 2, 3]
prime_number = 11

print(word, numbers, prime_number)
# outprint: Hello [1, 2, 3] 11

# %%


def multiply_numbers(a, b):
    return a * b

# %%


def stringify(*items):
    print(f"got {items} in {type(items)}")
    return [str(item) for item in items]


# %%
stringify(1, "two", None)

# %%


def stringify_a(item0, *items):
    print(item0, items)


# %%
stringify_a(0)

stringify_a(0, 1)

# %%


def stringify_b(*items, item0):
    print(item0, items)


# %%
# expect error
stringify_b(0, 1)

# %%
stringify_b(0, item0=1)

# %%


def create_report(name, **grades):
    print(f"got {grades} in {type(grades)}")
    report_items = [f"***** Report Begin for {name} *****"]
    for subject, grade in grades.items():
        report_items.append(f"### {subject}: {grade}")
    report_items.append(f"***** Report End for {name} *****")
    print("\n".join(report_items))


# %%
create_report("John", math=100, phys=98, bio=95)

#####################################################################################
#
# 6.5	How do I write proper docstrings for a function?
#
#####################################################################################
# %%
help(isinstance)

# %%
print(isinstance.__doc__)

# %%


def doubler(a):
    """Return the number multiplied by 2"""
    return a * 2


# %%
def quotient(dividend, divisor, taking_int=False):
    """
    Calculate the product of two numbers with a base factor.

    :param dividend: int | float, the dividend in the division
    :param divisor: int | float, the divisor in the division
    :param taking_int: bool, whether only taking the integer part of the quotient; default: False, which calculates the precise quotient of the two numbers

    :return: float | int, the quotient of the dividend and divisor
    """
    result = dividend / divisor
    if taking_int:
        result = int(result)
    return result


# %%
# Expect the line to produce error
1 / 0

# %%


def quotient(dividend, divisor, taking_int=False):
    """
    Calculate the product of two numbers with a base factor.

    :param dividend: int | float, the dividend in the division
    :param divisor: int | float, the divisor in the division
    :param taking_int: bool, whether only taking the integer part of the quotient; default: False, which calculates the precise quotient of the two numbers

    :return: float | int, the quotient of the dividend and divisor

    :raises: ZeroDivisionError, when the divisor is 0
    """
    if divisor == 0:
        raise ZeroDivisionError("division by zero")  # A
    result = dividend / divisor
    if taking_int:
        result = int(result)
    return result
