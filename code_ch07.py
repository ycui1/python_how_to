def example():
    pass

example.__repr__()

numbers_str = ["1.23", "4.56", "7.89"]
numbers = list(map(float, numbers_str))
print(numbers)


def increment_maker(number):
    def increment(num0):
        return num0 + number

    return increment

increment_one = increment_maker(1)
increment_three = increment_maker(3)
increment_five = increment_maker(5)
increment_ten = increment_maker(10)


increment_one(99), increment_three(88), increment_five(80), increment_ten(100)

dir(increment_five)


from inspect import istraceback
from math import expm1
from os import sep
import random
import time
from tkinter import N

def example_func0():
    print("--- example_func0 starts")
    start_t = time.time()
    random_delay = random.randint(1, 5) * 0.1
    time.sleep(random_delay)
    end_t = time.time()
    print(f"*** example_func0 ends; used time: {end_t - start_t:.2f} s")


def example_func1():
    print("--- example_func1 starts")
    start_t = time.time()
    random_delay = random.randint(6, 10) * 0.1
    time.sleep(random_delay)
    end_t = time.time()
    print(f"*** example_func1 ends; used time: {end_t - start_t:.2f} s")

example_func0()
example_func1()


def logging_time(func):
    def logger(*args, **kwargs):
        print(f"--- {func.__name__} starts: ")
        start_t = time.time()
        value_returned = func(*args, **kwargs)
        end_t = time.time()
        print(f"*** {func.__name__} ends; used time: {end_t - start_t:.2f} s")
        return value_returned

    return logger

@logging_time
def example_func2():
    random_delay = random.randint(3, 5) * 0.1
    time.sleep(random_delay)


example_func2()

@logging_time
def example_func3():
    pass

@logging_time
def example_func4():
    pass

@logging_time
def example_func5():
    pass


def before():
    pass

after = logging_time(before)

after()

def outer(a):
    b = 5
    def inner():
        return a + b

    return inner

closure = outer(100)
closure

closure.__closure__[0].cell_contents
closure.__closure__[1].cell_contents

def monitor(func):
    def monitored():
        print(f"*** {func.__name__} is called")
        func()

    return monitored

@monitor
def example0():
    pass

example0()

@monitor
def example1(param0):
    pass

example1()

def say_hi(person):
    """Greet someone"""
    print(f"Hi, {person}")

@logging_time
def say_hello(person):
    """Greet someone"""
    print(f"Hello, {person}")

print(say_hi.__doc__, say_hi.__name__, sep="; ")
# output: 

print(say_hello.__doc__, say_hello.__name__, sep="; ")
# output: None

def logging_time_doc(func):
    def logger(*args, **kwargs):
        """Log the time"""
        print(f"--- {func.__name__} starts")
        start_t = time.time()
        value_returned = func(*args, **kwargs)
        end_t = time.time()
        print(f"*** {func.__name__} ends; used time: {end_t - start_t:.2f} s")
        return value_returned

    return logger

@logging_time_doc
def example_doc():
    """Example function"""
    pass

print(example_doc.__doc__)


import functools

def logging_time_wraps(func):
    @functools.wraps(func)
    def logger(*args, **kwargs):
        """Log the time"""
        print(f"--- {func.__name__} starts")
        start_t = time.time()
        value_returned = func(*args, **kwargs)
        end_t = time.time()
        print(f"*** {func.__name__} ends; used time: {end_t - start_t:.2f} s")
        return value_returned

    return logger

@logging_time_wraps
def example_wraps():
    """Example function"""
    pass

print(example_wraps.__doc__, example_wraps.__name__, sep="; ")


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

upper_limit = 1_000_000

squares_list = [x*x for x in range(1, upper_limit + 1)]

sum_list = sum(squares_list)

squares_list.__sizeof__()

def perfect_squares(limit):
    n = 1
    while n <= limit:
        yield n * n
        n += 1

squares_gen = perfect_squares(upper_limit)
sum_gen = sum(squares_gen)

assert sum_gen == sum_list == 333333833333500000

squares_gen = perfect_squares(upper_limit)
squares_gen.__sizeof__()

squares_gen_exp = (x * x for x in range(1, upper_limit))
squares_gen_exp

next(squares_gen_exp)
next(squares_gen_exp)
next(squares_gen_exp)

sum_gen_exp = sum(squares_gen_exp)
sum_gen_exp

sum(x*x for x in range(4))

def fibonacci_gen(limit):
    n, m = 0, 1
    while n <= limit:
        print(n, m)
        yield n
        n, m = m, m + n

list(fibonacci_gen(13))


def run_stats_model(dataset, model, output_path):
    # process the dataset
    # apply the model
    # save the stats to the output path
    calculated_stats = 123    #A
    return calculated_stats

from functools import partial

run_stats_model_a = partial(run_stats_model, model="model_a", output_path="project_a/stats/")

run_stats_model_a("dataset_a")

dir(run_stats_model_a)

run_stats_model_a.keywords
run_stats_model_a.func
run_stats_model_a.args

type((x for x in range(5)))

n = 1
while n < 3:
    print(f"n's value: {n}")
    n += 1

print(f"n's value after while loop: {n}")


def append_task(task, tasks=[]):
    tasks.append(task)
    print(f"Tasks: {tasks}; id: {id(tasks)}")    #A

append_task.__defaults__    #B
# output: ([],)

id(append_task.__defaults__[0])
# output: 4356663616

append_task("Homework")
# output: Tasks: ['Homework']; id: 4356663616

append_task("Laundry")
# output: Tasks: ['Homework', 'Laundry']; id: 4356663616

append_task.__defaults__
# output: (['Homework', 'Laundry'],)

from statistics import mean, stdev
from typing import Sequence


def generate_stats(measures: Sequence[float]) -> tuple[float, float]:
    measure_mean = mean(measures)
    measure_std = stdev(measures)
    return measure_mean, measure_std


generate_stats([1, 2, 3])

def example(**kwargs):
    pass

example(1, 2)

print(isinstance.__doc__)


