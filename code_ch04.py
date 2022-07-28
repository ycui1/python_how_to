#####################################################################################
#
# 4.1	How do I retrieve and manipulate subsequences with slice objects?
#
#####################################################################################
# %%
# str is a sequence of characters:
from timeit import timeit
from timeit import timeit  # B
from collections import deque  # A
from collections import deque
text = "Hello, World!"

# list is a mutable sequence of any kinds of objects
fruits = ["apple", "orange", "banana", "strawberry"]

# tuple is an immutable sequence of any kinds of objects
vowels = ("a", "e", "i", "o", "u")

# %%
assert fruits[1:3] == ["orange", "banana"]

assert fruits[:3] == ["apple", "orange", "banana"]

assert fruits[1:] == ["orange", "banana", "strawberry"]

# %%
# error is expected
fruits[5]
# ERROR: IndexError: list index out of range

# %%
numbers = [0, 1, 2, 3, 4, 5]
numbers[:20]  # A
# output: [0, 1, 2, 3, 4, 5]

numbers[-10000:2]  # B
# output: [0, 1, 2]


# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert numbers[2:5:2] == [3, 5]  # A

assert numbers[::3] == [1, 4, 7]  # B

assert numbers[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1]  # C

# %%
slice_obj = slice(1, 10, 2)
range_obj = range(1, 10, 2)

slice_obj.start, slice_obj.stop, slice_obj.step
# output: (1, 10, 2)

range_obj.start, range_obj.stop, range_obj.step
# output: (1, 10, 2)

# %%
list(range(10))
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(slice(10))
# error is expected for the above line

# %%
numbers = list(range(10))

odd_slice = slice(1, 10, 2)
numbers[odd_slice]
# output: [1, 3, 5, 7, 9]


odd_range = range(1, 10, 2)
numbers[odd_range]
# output error:


# %%
tasks = """
0....5..............20..........................48......
1001 Laundry        Wash all clothes            3
1002 Museum Visit   Go to the Egypt exhibit     4
1003 Do Homework    Physics and math            5
1004 Go to Gym      Work out for 1 hour         2
"""

# %%
task_id = slice(5)
task_title = slice(5, 20)
task_desc = slice(20, 48)
task_urgency = slice(48, 49)
task_lines = tasks.split("\n")[2:-1]
tasks = []
for line in task_lines:
    task = (line[task_id].strip(), line[task_title].strip(),
            line[task_desc].strip(), line[task_urgency].strip())  # A
    tasks.append(task)

print(tasks)

# %%
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers[:3] = [10, 11, 12]
numbers

# %%
numbers[3:] = [13, 14, 15, 16, 17, 18, 19, 20]
numbers

# %%
numbers[:5] = [0, 1]
numbers

# %%
numbers[::2] = [0, 0, 0, 0]
numbers

# %%
numbers = [0, 1, 0, 16, 0, 18, 0, 20]
del numbers[:4]
numbers
# output: [0, 18, 0, 20]

numbers[-2:] = []
numbers
# output: [0, 18]

#####################################################################################
#
# 4.2	How do I use positive and negative indexing to retrieve items?
#
#####################################################################################
# %%
revenue_by_month = [95, 100, 80, 93, 92, 110, 102, 88, 96, 98, 115, 120]
# %%
revenue_jan = revenue_by_month[0]  # A

revenue_season2 = revenue_by_month[3:6]  # B

# %%
revenue_nov = revenue_by_month[10]  # A

revenue_season4 = revenue_by_month[9:]  # B

# %%
revenue_nov_neg = revenue_by_month[-2]  # A
assert revenue_nov == revenue_nov_neg

revenue_season4_neg = revenue_by_month[-3:]  # B
assert revenue_season4 == revenue_season4_neg

# %%
revenue_middle = revenue_by_month[1:-1]  # A
revenue_middle
# output: [100, 80, 93, 92, 110, 102, 88, 96, 98, 115]


#####################################################################################
#
# 4.3	How do I find items in a sequence?
#
#####################################################################################

# %%
assert (8 in [1, 2, 3, 4, 5]) == False

assert ('cool' in 'Python is cool') == True

assert (404 in (404, 'Page Not Found')) == True

# %%
[1, 2, 3, 4, 5].index(4)
# output: 3

(404, 'Page Not Found').index('Page Not Found')
# output: 1

'Python is cool'.index('cool')
# output: 10

# %%
[1, 2, 3, 4, 5].index(8)
# error is expected

# %%
# some pseudo code


def process_item_try(item):
    try:
        item_index = the_list.index(item)
    except ValueError:
        # do something when the item isn’t present

        # do something with the item_index


def process_item_check_first(item):
    if item in the_list:
        item_index = the_list.index(item)


        # do something with the item_index
else:
    # do something when the item isn’t present

    # %%
    # some pseudo code


def find_string(substr):
    str_index = the_str.find(substr)
    if str_index >= 0:
        # do something with the str_index
    else:
        # do something when the substr isn’t present

        # %%


class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency


tasks = [
    Task("Laundry", 3),
    Task("Museum", 4),
    Task("Homework", 5),
    Task("Ticket", 2)
]

# %%


class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency


tasks = [
    Task("Laundry", 3),
    Task("Museum", 4),
    Task("Homework", 5),
    Task("Ticket", 2)
]

needed_urgency = 5
needed_task_index = None

for task_i in range(len(tasks)):  # A
    task = tasks[task_i]
    print(task.urgency)
    if task.urgency == needed_urgency:
        needed_task_index = task_i
        break

print(f"Task Index: {needed_task_index}")

# %%


class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency


tasks = [
    Task("Laundry", 3),
    Task("Museum", 4),
    Task("Homework", 5),
    Task("Ticket", 2)
]

needed_urgency = 5
needed_task_index = None

for task_i in range(len(tasks)):  # A
    if tasks[task_i].urgency == needed_urgency:
        needed_task_index = task_i
        break

print(f"Task Index: {needed_task_index}")
#####################################################################################
#
# 4.4	How do I unpack a sequence — beyond tuple unpacking?
#
#####################################################################################
# %%
task = (1001, "Laundry", 5)

task_id = task[0]
task_title = task[1]
task_urgency = task[-1]

# %%
task = (1001, "Laundry", 5)
task_id, task_title, task_urgency = task

print(task_id, task_title, task_urgency)
# output: 1001 Laundry 5

user_data = ("python_user", 35, "male")
username, age, gender = user_data
print(username, age, gender)
# output: python_user 35 male

# %%
x0, y0 = (90, 20)
(x1, y1) = 90, 20
(x2, y2) = (90, 20)

assert x0 == x1 == x2 == 90
assert y0 == y1 == y2 == 20

# %%
x3, y3 = 90, 20

assert x3 == 90
assert y3 == 20

# %%
player_scores = [6.1, 6.5, 6.8, 7.1, 7.3, 7.6, 8.2, 8.9]

lowest0 = player_scores[0]
middles0 = player_scores[1:-1]
highest0 = player_scores[-1]

final0 = sum(middles0) / len(middles0)

# %%
player_scores = [6.1, 6.5, 6.8, 7.1, 7.3, 7.6, 8.2, 8.9]
lowest1, middles1, highest1 = player_scores[0], player_scores[1:-
                                                              1], player_scores[-1]
final1 = sum(middles1) / len(middles1)
print(final1)
# %%
lowest2, *middles2, highest2 = player_scores  # A
final2 = sum(middles2) / len(middles2)

assert lowest0 == lowest2 == player_scores[0]
assert middles0 == middles2 == player_scores[1:-1]
assert highest0 == highest2 == player_scores[-1]

# %%
a, *b, c = "abcdefg"
b

# %%
first_score, *scores, last_score = [9.1, 8.9]
scores

# %%
# expect an error
score0, *scores0, *scores1, score1 = [9.1, 8.8, 9.2, 7.7, 8.4]


# %%
def update_status(t_id, t_status):  # A
    # use task_id to locate the task in the database and update its status
    pass


task = (1001, "Laundry", "Wash clothes", "completed")  # B
task_id, task_title, task_desc, task_status = task  # C

update_status(task_id, task_status)

# %%
task_id, _, _, task_status = task
# %%
task = (1001, "Laundry", "Wash clothes", "completed")
task_id, *_, task_status = task  # A

#####################################################################################
#
# 4.5	When should I consider alternative data models other than lists and tuples?
#
#####################################################################################
# %%
clients = list()


def check_in(client):
    clients.append(client)  # A
    print(f"in: New client {client} joined the queue.")


def connect_to_associate(associate):
    if clients:  # B
        client_to_connect = clients.pop(0)  # C
        print(f"out: Remove {client_to_connect}, connecting to {associate}.")
    else:
        print("No more clients are waiting.")


# %%


def time_fifo_testing(n):
    integer_l = list(range(n))
    integer_d = deque(range(n))
    t_l = timeit(lambda: integer_l.pop(0), number=n)
    t_d = timeit(lambda: integer_d.popleft(), number=n)  # C
    return f"{n: >9} list: {t_l:.6e} | deque: {t_d:.6e}"


numbers = (100, 1000, 10000, 100000)
for number in numbers:
    print(time_fifo_testing(number))

# %%

clients = deque()


def check_in(client):
    clients.append(client)
    print(f"in: New client {client} joined the queue.")


def connect_to_associate(associate):
    if clients:
        client_to_connect = clients.popleft()
        print(f"out: Remove {client_to_connect}, connecting to {associate}.")
    else:
        print("No more clients are waiting.")

# %%
