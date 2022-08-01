#####################################################################################
#
# 7.1	How do I use lambda functions for small jobs?
#
#####################################################################################
# %%
from functools import partial
import functools
import time
import random
lambda x: return x * 2

# ERROR: SyntaxError: invalid syntax

# %%


def doubler(x): return x * 2


# %%
print(type(doubler))
# output: <class 'function'>

# %%
doubler(5)

doubler(8)

# %%
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]


def using_urgency_level(task):
    return task['urgency']


tasks.sort(key=using_urgency_level, reverse=True)

# %%
tasks.sort(key=lambda x: x['urgency'], reverse=True)
tasks

# %%


def using_urgency_level(x): return x['urgency']


tasks.sort(key=using_urgency_level, reverse=True)

tasks

# %%


def using_urgency_level(x): return x['urgency']


tasks.sort(key=using_urgency_level, reverse=True)

# %%
# Expect the KeyError below


def using_urgency_level0(x): return x['urgency0']


tasks.sort(key=using_urgency_level0, reverse=True)

# %%
# Expect the KeyError below


def using_urgency_level1(task):
    return task['urgency1']


tasks.sort(key=using_urgency_level1, reverse=True)

# %%
integers = [-4, 3, 7, 0, -6]

sorted(integers, key=lambda x: abs(x))
# output: [0, 3, -4, -6, 7]

# %%
sorted(integers, key=abs)

# %%
scores = [(93, 95, 94), (92, 95, 96), (94, 97, 91), (95, 97, 99)]

max(scores, key=lambda x: x[0] + x[1] + x[2])
# output: (95, 97, 99)

# %%
max(scores, key=sum)


#####################################################################################
#
# 7.2	What're the implications of functions as objects?
#
#####################################################################################
# %%
def add_three(number):
    return number + 3


add_three(7)  # A


def greeting_message(person):
    return f"Hello, {person}!"


greeting_message("Zoe")  # B

# %%
tasks.sort(key=lambda x: x['urgency'], reverse=True)

# %%


def get_mean(data):
    return "mean of the data"


def get_min(data):
    return "min of the data"


def get_max(data):
    return "max of the data"


def process_data(data, action):
    if action == "mean":
        processed = get_mean(data)
    elif action == "min":
        processed = get_min(data)
    elif action == "max":
        processed = get_max(data)
    else:
        processed = "error in action"

    return processed


# %%
actions = {"mean": get_mean, "min": get_min, "max": get_max}


def fallback_action(data):  # A
    return "error in action"


def process_data(data, action):
    calculation = actions.get(action, fallback_action)
    processed = calculation(data)
    return processed


# %%
numbers_str = ["1.23", "4.56", "7.89"]

numbers = list(map(float, numbers_str))

assert numbers == [1.23, 4.56, 7.89]


# %%
numbers_list = [float(x) for x in numbers_str]

# %%


def outside(x):
    def inside(y):
        pass
    pass

# %%


def increment_maker(number):
    def increment(num0):
        return num0 + number

    return increment


# %%
increment_one = increment_maker(1)
increment_three = increment_maker(3)
increment_five = increment_maker(5)
increment_ten = increment_maker(10)

increment_one(99), increment_three(88), increment_five(80), increment_ten(100)
# output: (100, 91, 85, 110)

#####################################################################################
#
# 7.3	How do I check functions' performance with decorators?
#
#####################################################################################
# %%


def example_func0():
    print("--- example_func0 starts")
    start_t = time.time()
    random_delay = random.randint(1, 5) * 0.1  # A
    time.sleep(random_delay)  # A
    end_t = time.time()
    print(f"*** example_func0 ends; used time: {end_t - start_t:.2f} s")


def example_func1():
    print("--- example_func1 starts")
    start_t = time.time()
    random_delay = random.randint(6, 10) * 0.1  # B
    time.sleep(random_delay)  # B
    end_t = time.time()
    print(f"*** example_func1 ends; used time: {end_t - start_t:.2f} s")


# %%
example_func0()

example_func1()

# %%


def logging_time(func):
    def logger(*args, **kwargs):
        print(f"--- {func.__name__} starts")
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


# %%
@logging_time
def example_func3():
    pass


@logging_time
def example_func4():
    pass


@logging_time
def example_func5():
    pass

# %%


def logging_time_backbone(func):
    def logger(*args, **kwargs):
        # covering the body's details later
        pass

    return logger

# %%


def before_deco():
    pass


after_deco = logging_time(before_deco)

after_deco()

# %%


def monitor(func):
    def monitored():
        print(f"*** {func.__name__} is called")
        func()

    return monitored

# %%


@monitor
def example0():
    pass


example0()


# %%
# Expect the code to fail
@monitor
def example1(param0):
    pass


example1("a string")

# %%


def say_hi(person):
    """Greet someone"""
    print(f"Hi, {person}")


@logging_time
def say_hello(person):
    """Greet someone"""
    print(f"Hello, {person}")


print(say_hi.__doc__, say_hi.__name__, sep="; ")
# output: Greet someone; say_hi

print(say_hello.__doc__, say_hello.__name__, sep="; ")
# output: None; logger


# %%
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
# output: Log the time


# %%


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
# output: Example function; example_wraps


#####################################################################################
#
# 7.4	How can I use generator functions as a memory-efficient data provider?
#
#####################################################################################
# %%
upper_limit = 1_000_000

squares_list = [x*x for x in range(1, upper_limit + 1)]  # A

sum_list = sum(squares_list)

# %%
print(squares_list.__sizeof__())

# output: 8448712    #A


# %%
def perfect_squares(limit):
    n = 1
    while n <= limit:
        yield n * n
        n += 1


squares_gen = perfect_squares(upper_limit)

sum_gen = sum(squares_gen)

assert sum_gen == sum_list == 333333833333500000


# %%
squares_gen = perfect_squares(upper_limit)

print(squares_gen.__sizeof__())
# output: 88    #A

# %%
squares_gen_exp = (x * x for x in range(1, upper_limit))
squares_gen_exp

# %%
next(squares_gen_exp)
next(squares_gen_exp)
next(squares_gen_exp)

# %%
sum_gen_exp = sum(squares_gen_exp)
sum_gen_exp

#####################################################################################
#
# 7.5	How do I create partial functions to make routine function calls easier?
#
#####################################################################################
# %%


def run_stats_model(dataset, model, output_path):
    # process the dataset
    # apply the model
    # save the stats to the output path
    calculated_stats = 123  # A
    return calculated_stats


# %%
# Project A
run_stats_model(dataset_a1, "model_a", "project_a/stats/")
run_stats_model(dataset_a2, "model_a", "project_a/stats/")
run_stats_model(dataset_a3, "model_a", "project_a/stats/")
run_stats_model(dataset_a4, "model_a", "project_a/stats/")

# Project B
run_stats_model(dataset_b1, "model_b", "project_b/stats/")
run_stats_model(dataset_b2, "model_b", "project_b/stats/")
run_stats_model(dataset_b3, "model_b", "project_b/stats/")
run_stats_model(dataset_b4, "model_b", "project_b/stats/")

# Project C
run_stats_model(dataset_c1, "model_c", "project_c/stats/")
run_stats_model(dataset_c2, "model_c", "project_c/stats/")
run_stats_model(dataset_c3, "model_c", "project_c/stats/")
run_stats_model(dataset_c4, "model_c", "project_c/stats/")

# %%


def run_stats_model_a(dataset):
    model_stats = run_stats_model(dataset, "model_a", "project_a/stats/")
    return model_stats


# %%
# Project A
run_stats_model_a(dataset_a1)
run_stats_model_a(dataset_a2)
run_stats_model_a(dataset_a3)
run_stats_model_a(dataset_a4)

# %%

run_stats_model_a = partial(
    run_stats_model, model="model_a", output_path="project_a/stats/")

run_stats_model_a("dataset_a")
# output: 123
