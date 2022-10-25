#####################################################################################
#
# 3.1	How do I choose between lists and tuples?
#
#####################################################################################
#%%
numbers = [1, 2, 3]

numbers.insert(0, 0)    #A
# numbers becomes [0, 1, 2, 3]

numbers.append(4)    #B
# numbers becomes [0, 1, 2, 3, 4]

numbers.extend([5, 6, 7])    #C
# numbers becomes: [0, 1, 2, 3, 4, 5, 6, 7]

numbers.remove(5)    #D
# numbers becomes [0, 1, 2, 3, 4, 6, 7]

del numbers[3]    #E
# numbers becomes [0, 1, 2, 4, 6, 7]

# %%
# The following lines are expected not to run.
integers_tuple = (1, 2, 3)
integers_tuple.append(4)    #A
integers_tuple[0] = 'zero'    #B

#####################################################################################
#
# 3.2	How do I sort lists of complicated data using custom functions?
#
#####################################################################################
#%%
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

#%%
# expect errors
tasks.sort()

# %%
numbers = [12, 4, 1, 3, 7, 5, 9, 8]
numbers.sort()    #A
print(numbers)
# output: [1, 3, 4, 5, 7, 8, 9, 12]

names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort(reverse=True)    #B
print(names)
# output: ['Zack', 'Mike', 'Jennifer', 'David', 'Danny', 'Aaron']

mixed = [3, 1, 2, 'John',  ['c', 'd'], ['a', 'b']]
mixed.sort()
# error is expected for the above line

#%%
mixed = [3, 1, 2, 'John',  ['c', 'd'], ['a', 'b']]
mixed.sort(key=str)

print(mixed)

#%%
def using_urgency_level(task):
    return task['urgency']

tasks.sort(key=using_urgency_level, reverse=True)
print(tasks)

#####################################################################################
#
# 3.3	How do I build a lightweight data model using named tuples?
#
#####################################################################################
# %%
task_list = ['Laundry', 'Wash clothes', 3]    #A

task_tuple = ('Laundry', 'Wash clothes', 3)    #B

task_dict = {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}    #C

#%%
class Task:    #D
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
    
task_class = Task('Laundry', 'Wash clothes', 3)

# %%
from collections import namedtuple

Task = namedtuple('Task', 'title desc urgency')    #A
task_nt = Task('Laundry', 'Wash clothes', 3)    #B

assert task_nt.title == 'Laundry'    #C
assert task_nt.desc == 'Wash clothes'   #C

# %%
assert issubclass(Task, tuple) == True

# %%
Task = namedtuple('Task', 'title, desc, urgency')

Task = namedtuple('Task', ['title', 'desc', 'urgency'])

#%%
task_data = '''Laundry,Wash clothes,3
Homework,Physics + Math,5
Museum,Epyptian things,2'''

# %%
for task_text in task_data.split('\n'):    #A
    title, desc, urgency = task_text.split(',')    #B
    task_nt = Task(title, desc, int(urgency))
    print(f"--> {task_nt}")

# %%
for task_text in task_data.split('\n'):
    task_nt = Task._make(task_text.split(','))

#####################################################################################
#
# 3.4	How do I access dictionary keys, values, and items?
#
#####################################################################################
# %%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgen_keys = urgencies.keys()
urgen_values = urgencies.values()
urgen_items = urgencies.items()
print(urgen_keys, urgen_values, urgen_items, sep="\n")

# %%
urgencies["Grocery Shopping"] = 4

print(urgen_keys)
# output: dict_keys(['Laundry', 'Homework', 'Museum', 'Grocery])

print(urgen_values)
# output: dict_values([3, 5, 2, 4])

print(urgen_items)
# output: dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2), ('Grocery, 4)])

#%%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}

urgen_keys_list = list(urgencies.keys())
print(urgen_keys_list)
# output: ['Laundry', 'Homework', 'Museum']

urgencies["Grocery"] = 4
print(urgen_keys_list)
# output: ['Laundry', 'Homework', 'Museum']

#%%
assert urgencies["Laundry"] == 3

assert urgencies["Homework"] == 5

#%%
# expecting an error
urgencies["Homeworks"]

#%%
if "Homework" in urgencies:    #A
    urgency = urgencies["Homework"]
else:
    urgency = "N/A"

# %%
def retrieve_urgency(task_title):
    if task_title in urgencies:
        urgency = urgencies[task_title]
    else:
        urgency = "N/A"
    return urgency

# %%
retrieve_urgency("Homework")
# output: 5

retrieve_urgency("Homeworks")
# output: 'N/A'

# %%
urgencies.get("Homework")
# output: 5

urgencies.get("Homeworks", "N/A")
# output: 'N/A'

urgencies.get("Homeworks")
# output: None (None is automatically hidden in an interactive console)

#%%
# some pseudo code
def calculate_something(arg0, arg1, **kwargs):
    kwarg0 = kwargs.get("kwarg0", 0)
    kwarg1 = kwargs.get("kwarg1", "normal")
    kwarg2 = kwargs.get("kwarg2", [])
    kwarg3 = kwargs.get("kwarg3", "text")
    # ... and so on

# possible invocations:
calculate_something(arg0, arg1)
calculate_something(arg0, arg1, kwarg0=5)
calculate_something(arg0, arg1, kwarg0=5, kwarg3="text")

#%%
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgencies.setdefault("Homework")
# output: 5

urgencies.setdefault("Homeworks", 0)
# output: 0

urgencies.setdefault("Grocery")
# output: None (None is automatically hidden in an interactive console)

# %%
urgencies
# %%
urgencies["Homeworks"] = 0
urgencies["Grocery"] = None


#####################################################################################
#
# 3.5	When do I use dictionaries and sets instead of lists and tuples?
#
#####################################################################################
#%%
# errors are expected
failed_dict = {[0, 2]: "even"}
failed_set = {{"a": 0}}

#%%
from timeit import timeit

for count in [10, 100, 1000, 10000, 100000]:
    setup_str = f"""from random import randint; n = {count}; numbers_set = set(range(n)); numbers_list = list(range(n))"""    #A
    stmt_set = "randint(0, n-1) in numbers_set"    #B
    stmt_list = "randint(0, n-1) in numbers_list"    #C
    t_set = timeit(stmt_set, setup=setup_str, number=10000)    #D
    t_list = timeit(stmt_list, setup=setup_str, number=10000)    #D
    print(f"{count: >6}: {t_set:e} vs. {t_list:e}")

#%%
hash("Hello World!")    #A
# output: 9222343606437197585

hash(100)
# output: 100

hash([1, 2, 3])
# ERROR: TypeError: unhashable type: 'list'


# %%
from collections.abc import Hashable

def check_hashability():
    items = [{"a": 1}, [1], {1}, 1, 1.2, "test", (1, 2), True, None]    #A
    for item in items:
        print(f"{str(type(item)): <18} | {isinstance(item, Hashable)}")    #B

print(f"{'Data Type': <18}  {'Hashable'}")
check_hashability()

#%%
text = "Hello, World."
text[-1] = "!"
# error is expected

#%%
text.replace(".", "!")



#####################################################################################
#
# 3.6	How do I use set operations to check the relationships between lists?
#
#####################################################################################
#%%
good_stocks = ["AAPL", "GOOG", "AMZN", "NVDA"]
client0 = ["GOOG", "AMZN"]
client1 = ["AMZN", "SNAP"]

# %%
def all_contained_in_recommended(recommended, personal):
    print(f"Is {personal} contained in {recommended}?")
    for stock in personal:
        if stock not in recommended:    #A
            return False
    return True

# %%
print(all_contained_in_recommended(good_stocks, client0))
print(all_contained_in_recommended(good_stocks, client1))



# %%
good_stocks_set = set(good_stocks)    #A

contained0 = good_stocks_set.issuperset(client0)    #B
print(f"Is {client0} contained in {good_stocks}? {contained0}")
# output: Is ['GOOG', 'AMZN'] contained in ['AAPL', 'GOOG', 'AMZN', 'NVDA']? True

contained1 = good_stocks_set.issuperset(client1)
print(f"Is {client1} contained in {good_stocks}? {contained1}")
# output: Is ['AMZN', 'SNAP'] contained in ['AAPL', 'GOOG', 'AMZN', 'NVDA']? False



# %%
def contained_any_in_recommended(recommended, personal):
    print(f"Does {personal} contain any in {recommended}?")
    for stock in personal:
        if stock in recommended:
            return True
    return False

# %%
print(contained_any_in_recommended(good_stocks, client0))
print(contained_any_in_recommended(good_stocks, client1))

# %%
good_stocks_set & set(client0)
# output: {'AMZN', 'GOOG'}

bool(good_stocks_set & set(client0))
# output: True

good_stocks_set & set(client1)
# output: {'AMZN'}

bool(good_stocks_set & set(client1))
# output: True

#%%
good_stocks_set.intersection(client0)
# output: {'AMZN', 'GOOG'}

good_stocks_set.intersection(client1)
# output: {'AMZN'}

#%%
tasks_a = {"Homework", "Laundry", "Grocery"}
tasks_b = {"Laundry", "Gaming"}


tasks_a | tasks_b    #A
# output: {'Laundry', 'Gaming', 'Homework', 'Grocery'}

tasks_a & tasks_b    #B
# output: {'Laundry'}

tasks_a ^ tasks_b    #C
# output: {'Homework', 'Grocery', 'Gaming'}

tasks_a - tasks_b    #D
# output: {'Homework', 'Grocery'}


# %%
small_set = {1, 2}
large_set = {1, 2, 3, 4}

assert small_set.issubset(large_set) == True
assert small_set.issuperset(large_set) == False

assert large_set.issubset(small_set) == False
assert large_set.issuperset(small_set) == True



