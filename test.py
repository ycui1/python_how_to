# %%
from ast import Try, match_case
from collections import namedtuple

from numpy import integer

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

    # task_nt = Task(title, desc, int(urgency))
    # print(f"--> {task_nt}")

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

for item in numbers[odd_slice]:
    print(item*item)
# %%
numeros = list(range(1, 10))
print(numeros)
print(list[2: 10])


# %%

# Procedural style
# line by line
# uso de sentencias
# Uso de expresiones
# funciones extensas

OPERADORES = ('+', '-', '*', '/')

print(OPERADORES)


def calculadora_procedural():
    num1 = leer_numero()
    operador = leer_operador()
    num2 = leer_numero()
    res = calcular(num1, operador, num2)
    print(f"El resultado es: {res}")


def leer_numero():
    while True:
        num_str = input('Dame un numero: ')
        try:
            return int(num_str)
        except:
            print('Captura un número entero')


def leer_operador():
    while True:
        op = input('Dame la operación [+,-,*,/]: ')
        if op in OPERADORES:
            return op
        print("Operación inválida")


def calcular(num1, operador, num2):

    match operador:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            return num1/float(num2)
        case '_':
            return "No se puede realizar la operación"


calculadora_procedural()
# %%

# Functional style
# Pocas sentencias (no for)
# uso extensivo de expresiones
# Funciones sencillas

OPERADORES = ('+', '-', '*', '/')

print(OPERADORES)


def calculadora_funcional():
    return calcular(
        leer_numero(),
        leer_operador(),
        leer_numero(),
    )


def leer_numero():
    while True:
        num_str = input('Dame un numero: ')
        try:
            return int(num_str)
        except:
            print('Captura un número entero')


def leer_operador():
    while True:
        op = input('Dame la operación [+,-,*,/]: ')
        if op in OPERADORES:
            return op
        print("Operación inválida")


def calcular(num1, operador, num2):

    match operador:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            return num1/float(num2)
        case '_':
            return "No se puede realizar la operación"


print(f"El resultado es: {calculadora_funcional()}")

# %%

OPERADORES = ('+', '-', '*', '/')

print(OPERADORES)


def calculadora_funcional():
    return calcular(
        leer_numero(),
        leer_operador(),
        leer_numero(),
    )


def leer_numero():
    return int(input('Dame un numero: '))


def leer_operador():
    return input('Dame la operación [+,-,*,/]: ')


def calcular(num1, operador, num2):

    return num1+num2 if operador == '+'\
        else num1-num2 if operador == '-'\
        else num1*num2 if operador == '*'\
        else num1/float(num2) if operador == '/'\
        else "No se puede realizar la operación"


print(f"El resultado es: {calculadora_funcional()}")

# %%


def cuad(n):
    return n*n


n1, n2 = cuad(
    cuad(4)
), 5
print(n1, n2)
# %%
start, end, *nums = [1, 10, 2, 3, 4, 5, 6, 7, 8]
print(f"Start: {start}")
print(f"End: {end}")
print(f"Values: {nums}")

# %%
*nums, start, end = [2, 3, 4, 5, 6, 7, 8, 1, 10]
print(f"Start: {start}")
print(f"End: {end}")
print(f"Values: {nums}")

# %%
numbers = [i for i in range(1, 4)]
squares1 = [i*i for i in numbers]
print(squares1)

squares2 = [i*i for i in [i for i in range(1, 4)]]
print(squares2)


def square(n):
    return n*n


squares3 = [square(i) for i in [i for i in range(1, 4)]]
print(squares3)

# %%

Task = namedtuple("Task", "title description" "urgency")
tasks = [
    Task("Homework", "Physics and math", 5),
    Task("Laundry", "Wash clothes", 3),
    Task("Museum", "Egypt exhibit", 4)
]
tasks

# %%
nums = [3, 1, 5, 4, 7, 8, 9]
for i, item in enumerate(nums, start=1):
    print(f"1:{i}*{item}={i*item}")

for i, item in enumerate(range(1, 10), start=1):
    print(f"2:{i}*{item}={i*item}")

for i in range(1, 11):
    print(f"3:{i}*{i}={i*i}")

# %%


def sumar(a, b=1):
    return a+b


print(sumar.__defaults__)
# %%


def no_return():
    pass


res = no_return()
print(res)

# %%


def calculate_sum(a: int, b: int) -> int:
    return a+b


# calculate_sum()
calculate_sum("2", 3)

# %%


def calculate(a: int, b: int) -> list[int, int, int, float]:
    return [a+b, a-b, a*b, a/b]


res = calculate(2, 3)
print(res)


# %%
def sumar(*nums, k):
    for item in nums:
        print(item*k)


sumar(1, 2, 3, 4, 5, k=10)
# sumar(k=10, 1, 2, 3, 4, 5)

# %%


def sumar(*nums, k) -> list:
    return [num*k for num in nums]


print(sumar(1, 2, 3, 4, 5, k=10))

# %%


def hello(msg: str = ""):
    print(msg)


print(hello().__class__)
print(hello().__init__)

# %%


def using_urgency_level(x): return x['urgency']


tasks.sort(key=using_urgency_level, reverse=True)


# %%
def calculate(a, b): return [a+b, a-b, a*b, a/b]


print(res := calculate(2, 3))

# %%

nums = [(5, 4), (6, 4), (3, 2), (3, 10)]


def my_sum(n): return n[0]+n[1]


max_pair = max(nums, key=my_sum)
print(max_pair)


pow(4, 2)


nums = [5, 4, 3, 6, 3, 2, 10]


def max_square(n): return n*n


max_square = max(nums, key=max_square)
print(max_square)

nums = [[5, 2], [6, 2], [3, 2], [8, 2]]

nums = [5, 4, 3, 6, 3, 2, 10]

max_square = max(nums, key=pow(2))
print(max_square)

# %%
my_dict = {
    "pair1": (2, 4),
    "pair2": (4, 6),
    (1, 2): "tuple"
}

my_dict

# %%


def get_mean(data):
    return "mean of the data"


def get_min(data):
    return "min of the data"


def get_max(data):
    return "max of the data"


def process_data(data, action):
    match action:
        case "mean":
            processed = get_mean(data)
        case "min":
            processed = get_min(data)
        case "max":
            processed = get_max(data)
        case _ :
            processed = "error in action"

    return processed

# %%
