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

from numpy import number
numbers = ([1, 2], [1, 2])
print(numbers)
numbers[0].append(3)
print(numbers)

# %%
age = 50
name = "Alex"
my_tupla = (age, name)

print(my_tupla[1])

# %%
