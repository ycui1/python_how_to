class Task:
    def __init__(self, title, description, urgency):
        self.title = title
        self.description = description
        self.urgency = urgency
        

def complete_task(task):
    task.status = "completed"
    print(f"{task.title}'s status: {task.status}")

task = Task("Homework", "Physics and math", 5)
complete_task(task)


def complete_task(task, grouped_tasks=[]):
    task.status = "completed"
    grouped_tasks.append(task.title)
    return grouped_tasks
    

task0 = Task("Homework", "Physics and math", 5)
work_tasks = complete_task(task0)

task1 = Task("Fishing", "Fishing at the lake", 3)
play_tasks = complete_task(task1)

print("Work Tasks:", work_tasks)
print("Play Tasks:", play_tasks)

assert work_tasks == play_tasks
assert work_tasks is play_tasks


def append_task(task, tasks=[]):
    tasks.append(task)
    print(f"Tasks: {tasks}; id: {id(tasks)}")
    
append_task.__defaults__
id(append_task.__defaults__[0])
append_task("Homework")
append_task("Laundry")


def complete_task(task, grouped_tasks=None):
    task.status = "completed"
    if grouped_tasks is None:
        grouped_tasks = []
    grouped_tasks.append(task.title)
    return grouped_tasks

complete_task.__defaults__

from datetime import datetime
import statistics

datetime.today()


numbers = list(range(5))
sum_numbers = sum(numbers)
print(f"Sum of {numbers} is {sum_numbers}")

primes = [5, 7, 2, 3, 11]
sorted_primes = primes.sort()
print(f"Sorted: {sorted_primes}")


def append_task(task, grouped_tasks):
    grouped_tasks.append(task)
    
appended = append_task("Homework", [])
print(f"Appended: {appended}")

from statistics import mean, stdev

def generate_stats(measures):
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std

def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean

def calculate_std(measures):
    measure_std = stdev(measures)
    return measure_std

def process_data(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    measure_mean = mean(measures)
    return formatted_measures, measure_mean

def format_measures(measures):
    formatted_measures = [f"{x} mg/L" for x in measures]
    return formatted_measures

def calculate_mean(measures):
    measure_mean = mean(measures)
    return measure_mean

measures = [5.6, 7.0, 5.7, 5.8, 4.3, 5.2]
measures_stats = generate_stats(measures)
print(type(measures_stats), measures_stats)

m_mean, m_std = generate_stats(measures)
print(f"Mean: {m_mean}; SD: {m_std}")

number = 1
print(type(number))

number = "one"
print(type(number))

number: int = 3

name: str = "John"

primes: list = [2, 3, 5]

numbers: tuple = (1, 2, 3)
numbers = [1, 2, 3]


from statistics import mean, stdev

def generatate_stats(measures: list) -> tuple:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std

help(generatate_stats)


word = "Hello"
numbers = [1, 2, 3]
prime_number = 11
print(word, numbers, prime_number)

def multiply_numbers(a, b):
    return a * b

multiply_numbers(1, 2)
multiply_numbers(1, b=2)

multiply_numbers(a=1, b=2)
multiply_numbers(b=1, a=2)

multiply_numbers(b=6, 5)

def stringify(*items):
    print(f"got {items} in {type(items)}")
    return [str(item) for item in items]

stringify(1, "two", None)

def stringify_a(item0, *items):
    print(item0, items)

stringify_a(0)
stringify_a(0, 1)

def stringify_b(*items, item0):
    print(item0, items)

stringify_b(0, 1)

stringify_b(0, item0=1)

def create_report(name, **grades):
    print(f"got {grades} in {type(grades)}")
    report_items = [f"***** Report Begin for {name} *****"]
    for subject, grade in grades.items():
        report_items.append(f"### {subject}: {grade}")
    report_items.append(f"***** Report End for {name} *****")
    print("\n".join(report_items))

create_report("John", math=100, phys=98, bio=95)

def example(**kwargs):
    pass

example(a=1, b=2)
example(1, 2)
example(2a=1, 2b=2)
example()

help(list)

list()

print(isinstance.__doc__)

def example(arg0, arg1):
    """This is an example function docstring.
    
    Args:
        arg0:
        arg1:

    Returns:
        Describe the return value

    Raises:
        Describe any Exception
    """
    pass

print(example.__doc__)

import pathlib

def doubler(a: int):
    """Return the number multiplying 2"""
    return a * 2


doubler.__annotations__

doubler.__code__

doubler.__doc__

doubler.__dir__()


def example(a: str, b: int) -> bool:
    return True

example.__annotations__

def multiplier(num1: float, num2: float) -> float:
    """Multiply two numbers to get their product.
    
    :param num1: float, first number for multiplication
    :param num2: float, second number for multiplication

    :return: float, the product of the two numbers
    """
    return num1 * num2

print(multiplier.__doc__)

def example(a, b=1, c="Hello!"):
    print(a, b, c)

example("Hi")
example("Hi", 2, "Python")

example.__defaults__


def example(a, b=list()):
    pass

example.__defaults__


def outer(a):
    def inner():
        b = a + 1
        return b

    return inner

closure = outer(5)
closure.__closure__


def multiplier_creator(n):
    def multiplier(number):
        return number * n

    return multiplier


double_multiplier = multiplier_creator(2)
triple_multiplier = multiplier_creator(3)


a = double_multiplier.__closure__

type(a)

double_multiplier.__closure__[0].cell_contents

lambda x: return x * 2


doubler = lambda x: x * 2
type(doubler)

doubler(5)
doubler(8)

