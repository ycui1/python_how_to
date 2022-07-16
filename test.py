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

list_str = "[1, 2, 3, 4]"
stripped_str = list_str.strip("[]")
print(stripped_str)

number_list = [int(x) for x in stripped_str.split(",")]
print(number_list)
