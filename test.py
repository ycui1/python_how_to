""" def cast_number(number_str):
    try:
        casted_number = float(number_str)
    except ValueError:
        print(f"Couldn't cast {repr(number_str)} to a number")  # A
    else:
        print(f"Casting {repr(number_str)} to {casted_number}")
 """

# python -i test.py
# import importlib
# importlib.reload(test)

""" list_str = "[1, 2, 3, 4]"
stripped_str = list_str.strip("[]")
print(stripped_str)

number_list = [int(x) for x in stripped_str.split(",")]
print(number_list)
 """

# %%
""" import sys
mi_Lista = [3.1416, "Hola"]
mi_Tupla = (3.1416, "Hola")

print(sys.getsizeof(mi_Lista))
print(sys.getsizeof(mi_Tupla))
# Output
# 72
# 56 """
# %%
""" 
age = 50
name = "Alex"
my_tupla = (age, name)

print(my_tupla)

age = 30
name = "Alexander"

print(age, name)

print(my_tupla)

# output
# (50, 'Alex')
# 30 Alexander
# (50, 'Alex') """

# %%

""" from numpy import number
numbers = ([1, 2], [1, 2])
print(numbers)
numbers[0].append(3)
print(numbers)

# %%
age = 50
name = "Alex"
my_tupla = (age, name)

print(my_tupla[1])
 """

# %%
""" 
from collections import namedtuple
task_list = ['Laundry', 'Wash clothes', 3]  # A
task_tuple = ('Laundry', 'Wash clothes', 3)  # B
task_dict = {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}  # C


class Task:  # D
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency


task_class = Task('Laundry', 'Wash clothes', 3)
Task = namedtuple('Task', 'title desc urgency')  # A
task_nt = Task('Laundry', 'Wash clothes', '3')  # B
Task = namedtuple('Task', 'title, desc, urgency')
Task = namedtuple('Task', ['title', 'desc', 'urgency'])
task_data = '''Laundry,Wash clothes,3
Homework,Physics + Math,5
Museum,Epyptian things,2'''

for task_text in task_data.split('\n'):  # A
    print(task_text)
    print(task_text.split(','))
    print("-------------------------")

print("==================================")
for task_text in task_data.split('\n'):  # A
    title, desc, urgency = task_text.split(',')  # B
    print(title, desc, urgency)

    #task_nt = Task(title, desc, int(urgency))
    #print(f"--> {task_nt}")

for task_text in task_data.split('\n'):
    task_nt = Task._make(task_text.split(','))
 """
# %%
""" data = [1, 2, 3]
x, y, z = data
print(x, y, z) """

# %%
""" 

from numpy import number
my_set = {1, 2, 2, 3, 4, 5}
print(my_set)
# %%
k1: int = "1"
k2: float = "1.0"
numbers = {k1: "one", k2: "one point zero"}
print(numbers)"""
# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numbers[::2])
print(numbers[1::2])

print(numbers2[::2])
print(numbers2[1::2])

# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[8:2:-1])

print(numbers[::-1][1:7])

# %%
pares = sum(list(range(2, 12, 2)))
print(pares)
# %%
numbers = list(range(10))

odd_slice = slice(1, 10, 2)
print(sum(numbers[odd_slice]))

print(odd_slice)


# %%
