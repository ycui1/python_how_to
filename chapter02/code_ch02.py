#####################################################################################
#
# 2.1	How do I use f-strings for string interpolation and formatting?
#
#####################################################################################

#%%
# existing variables
name = "Homework"
urgency = 5

# desired output:
Name: Homework; Urgency Level: 5

# Note: the above line isn't supposed to run as Python code, as it's text output.

#%%
task = "Name: " + name + "; Urgency Level: " + str(urgency)

print(task)
# output: Name: Homework; Urgency Level: 5

#%%
task1 = "Name: %s; Urgency Level: %d" % (name, urgency)

task2 = "Name: {}; Urgency Level: {}".format(name, urgency)

#%%
task_f = f"Name: {name}; Urgency Level: {urgency}"

assert task == task_f == "Name: Homework; Urgency Level: 5"

#%%
tasks = ["homework", "laundry"]
assert f"Tasks: {tasks}" == "Tasks: ['homework', 'laundry']"    #A

task_hwk = ("Homework", "Complete physics work")
assert f"Task: {task_hwk}" == "Task: ('Homework', 'Complete physics work')"    #B

task = {"name": "Laundry", "urgency": 3}
assert f"Task: {task}" == "Task: {'name': 'Laundry', 'urgency': 3}"    #C

#%%
tasks = ["homework", "laundry", "grocery shopping"]
assert f"First Task: {tasks[0]}" == 'First Task: homework'    #A

task_name = "grocery shopping"
assert f"Task Name: {task_name.title()}" == 'Task Name: Grocery Shopping'    #B

number = 5
assert f"Square: {number*number}" == 'Square: 25'    #C

# %%
summary_text = f"Your Average Score: {sum([95, 98, 97, 96, 97, 93]) / len([95, 98, 97, 96, 97, 93])}."

# %%
scores = [95, 98, 97, 96, 97, 93]
total_score = sum(scores)
subject_count = len(scores)
average_score = total_score / subject_count
summary_text = f"Your Average Score: {average_score}."

# %%
task_ids = [1, 2, 3]
task_names = ['Do homework', 'Laundry', 'Pay bills']
task_urgencies = [5, 3, 4]

for i in range(3):
    print(f'{task_ids[i]:^12}{task_names[i]:^12}{task_urgencies[i]:^12}')

# %%
def create_formatted_records(fmt):
    for i in range(3):
        print(f'{task_ids[i]:{fmt}}{task_names[i]:{fmt}}{task_urgencies[i]:{fmt}}')

# %%
create_formatted_records('^15')

# %%
create_formatted_records('^18')

# %%
large_prime_number = 1000000007

print(f"Use commas: {large_prime_number:,d}")
# output: Use commas: 1,000,000,007


# %%
decimal_number = 1.23456

print(f"Two digits: {decimal_number:.2f}")
# output: Two digits: 1.23

print(f"Four digits: {decimal_number:.4f}")
# output: Four digits: 1.2346

# %%
sci_number = 0.00000000412733

print(f"Sci notation: {sci_number:e}")
# output: Sci notation: 4.1227330e-09

print(f"Sci notation: {sci_number:.2e}")
# output: Sci notation: 4.13e-09

# %%
pct_number = 0.179323

print(f"Percentage: {pct_number:%}")
# output: Percentage: 17.932300%

print(f"Percentage two digits: {pct_number:.2%}")
# output: Percentage two digits: 17.93%


#####################################################################################
#
# 2.2	How do I convert strings to retrieve the represented data?
#
#####################################################################################
#%%
age = input("Please enter your age: ")

type(age)    #A

age > 18

#%%
bad_username0 = "123!@#"
assert bad_username0.isalnum() == False

bad_username1 = "abc..."
assert bad_username1.isalnum()== False

good_username = "1a2b3c"
assert good_username.isalnum() == True

# %%
assert "Homework".isalpha() == True

assert "Homework123".isalpha() == False

# %%
assert "123".isnumeric() == True

assert "a123".isnumeric() == False 


#%%
assert "3.5".isnumeric() == False

assert "-2".isnumeric() == False

#%%
float("3.25")
float("-2") 

int("-5")
int("123")

#%%
# The following code is expected to produce errors.
float("3.5a")
int("one")

#%%
def cast_number(number_str):
    try:
        casted_number = float(number_str)
    except ValueError:
        print(f"Couldn't cast {repr(number_str)} to a number")    #A
    else:
        print(f"Casting {repr(number_str)} to {casted_number}")

# Use the above function in a console
cast_number("1.5")
cast_number("2.3a")


#%%
# The following code is expected to produce errors.
numbers_list_str = "[1, 2]"
numbers_tuple_str = "(1, 2)"
numbers_dict_str = "{1:'one', 2: 'two'}" 

list(numbers_list_str)    #A
tuple(numbers_tuple_str)    #A
dict(numbers_dict_str)

#%%
assert eval(numbers_list_str) == [1, 2]

assert eval(numbers_tuple_str) == (1, 2)

assert eval(numbers_dict_str) == {1: 'one', 2: 'two'}

#%%
list_str = "[1, 2, 3, 4]"
stripped_str = list_str.strip("[]")
number_list = [int(x) for x in stripped_str.split(",")]

print(number_list)
# print out: [1, 2, 3, 4]


#####################################################################################
#
# 2.3	How do I join and split strings?
#
#####################################################################################
# %%
# initial input
fruit0 = "apple"
fruit1 = "banana"
fruit2 = "orange"

# desired output
liked_fruits = "apple, banana, orange"

# %%
# initial input
visited_countries = "United States, China, France, Canada"

# desired output
countries = ["United States", "China", "France", "Canada"]


# %%
style_settings = "font-size=large, " "font=Arial, " "color=black, " "align=center"

print(style_settings)
# output: font-size=large, font=Arial, color=black, align=center

# %%
settings = {"font_size": "large", "font": "Arial", "color": "black", "align": "center"}
styles = f"font-size={settings['font_size']}, " \
         f"font={settings['font']}, " \
         f"color={settings['color']}, " \
         f"align={settings['align']}"    #A

# %%
style_settings = ["font-size=large", "font=Arial", "color=black", "align=center"]
merged_style = ", ".join(style_settings)

print(merged_style)
# output: font-size=large, font=Arial, color=black, align=center


# %%
tasks = ["Homework", "Grocery", "Laundry", "Museum Trip", "Buy Furniture"]
note = ", ".join(tasks)

print("Remaining Tasks:", note)
# output: Remaining Tasks: Homework, Grocery, Laundry, Museum Trip, Buy Furniture


# %%
tasks.remove("Buy Furniture")
tasks.remove("Homework")

# %%
print("Remaining Tasks: ", ", ".join(tasks))
# output: Remaining Tasks:  Grocery, Laundry, Museum Trip


# %%
task_data = """1001,Homework,5
1002,Laundry,3
1003,Grocery,4"""

#%%
processed_tasks = []
for data_line in task_data.split("\n"):
    processed_task = data_line.split(",")
    processed_tasks.append(processed_task)
    
print(processed_tasks)

# %%
messy_data = "process,messy_data_mixed,separators"

separated_words0 = []
for word in messy_data.split(","):
    if word.find("_") < 0:    #A
        separated_words0.append(word)
    else:
        separated_words0.extend(word.split("_"))    #B

# %%
consolidated = messy_data.replace(",", "_")    #A
separated_words1 = consolidated.split("_")


#####################################################################################
#
# 2.4	What are the essentials of regular expressions?
#
#####################################################################################
#%%
import re

regex = re.compile(r"[,_]")    #A
separated_words2 = regex.split(messy_data)


# %%
import re

regex = re.compile("do")    #A
regex.pattern   #B
regex.search("do homework")   #C
regex.findall("don't do that")   #C


# %%
import re

re.search("pattern", "the string to be searched")
re.findall("pattern", "the string to be searched")

# %%
task_pattern = re.compile("\\\\task")
texts = ["\task", "\\task", "\\\task", "\\\\task"]
for text in texts:
    print(f"Match {text!r}: {task_pattern.match(text)}")

# %%
task_pattern_r = re.compile(r"\\task")
texts = ["\task", "\\task", "\\\task", "\\\\task"]
for text in texts:
    print(f"Match {text!r}: {task_pattern_r.match(text)}")


# %%
re.search(r"^hi", "hi Python")
# output: <re.Match object; span=(0, 2), match='hi'>

re.search(r"task$", "do the task")
# output: <re.Match object; span=(7, 11), match='task'>

re.search(r"^hi task$", "hi task")
# output: <re.Match object; span=(0, 7), match='hi task'>

re.search(r"^hi task$", "hi Python task")
# output: None (omitted output in an interactive console)

# %%
test_string = "h hi hii hiii hiiii"
test_patterns = [r"hi?", r"hi*", r"hi+", r"hi{3}", r"hi{2,3}", r"hi{2,}", 
                 r"hi??", r"hi*?", r"hi+?", r"hi{2,}?"]

for pattern in test_patterns:
    print(f"{pattern: <9}--->  {re.findall(pattern, test_string)}")

# %%
test_text = "#1$2m_ M\t"
patterns = ["\d", "\D", "\s", "\S", "\w", "\W", ".", "[lmn]"]
for pattern in patterns:
    print(f"{pattern: <9}--->  {re.findall(pattern, test_text)}")

# %%
re.findall(r"a|b", "a c d d b ab")
# output: ['a', 'b', 'a', 'b']

re.findall(r"a|b", "c d d b")
# output: ['b']

re.findall(r"(abc)", "ab bc abc ac")
# output: ['abc']

re.findall(r"(abc)", "ab bc ac")
# output: []

re.findall(r"[^a]", "abcde")
# output: ['b', 'c', 'd', 'e']

# %%
match = re.search(r"(\w\d)+", "xyza2b1c3dd")

print(match)
# output: <re.Match object; span=(3, 9), match='a2b1c3'>

# %%
print("matched:", match.group())
# output: matched: a2b1c3

print("span:", match.span())
# output: span: (3, 9)

print(f"start: {match.start()} & end: {match.end()}")
# output: start: 3 & end: 9

# %%
match = re.match("pattern", "string to match")
if match:
    print("do something with the matched")
else:
    print("found no matches")

# %%
match = re.match(r"(\w+), (\w+)", "Homework, urgent; today")
print(match)
# output: <re.Match object; span=(0, 16), match='Homework, urgent'>

match.groups()
# output: ('Homework', 'urgent')

match.group(0)
# output: 'Homework, urgent'

match.group(1)
# output: 'Homework'

match.group(2)
# output: 'urgent'


# %%
match.span(0)
# output: (0, 16)

match.span(1)
# output: (0, 8)

match.span(2)
# output: (10, 16)

# %%


#####################################################################################
#
# 2.5	How do I use regular expressions to process texts?
#
#####################################################################################
#%%
text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""    #A

# %%
regex = re.compile(r"(\d{3}), (\w+); (.+)")
for line in text_data.split("\n"):    #A
    match = regex.match(line)    #B
    if match:
        print(f"{'Matched:':<12}{match.group()}")    #C
    else:
        print(f"{'No Match:':<12}{line}")

# %%
regex = re.compile(r"(\d{3}), (\w+); (.+)")
tasks = []
for line in text_data.split("\n"):
    match = regex.match(line)
    if match:
        task = (match.group(1), match.group(2), match.group(3))    #A
        tasks.append(task)

print(tasks)

# %%
regex = re.compile(r"(?P<task_id>\d{3}), (?P<task_title>\w+); (?P<task_desc>.+)")
tasks = []
for line in text_data.split("\n"):
    match = regex.match(line)
    if match:
        task = (match.group('task_id'), match.group('task_title'), match.group('task_desc'))
        tasks.append(task)


# %%
match.groupdict()
# output: {'task_id': '101', 'task_title': 'Homework', 'task_desc': 'Complete physics and math'}
