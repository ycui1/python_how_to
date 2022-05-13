text_file = open("tasks.txt")
print(text_file)

print(type(text_file))

text_data = text_file.read()

print(type(text_data))

print(text_data)

text_file.close()
assert text_file.closed

text_file.read()

with open("tasks.txt") as file:
    print(f"file object: {file}")
    data = file.read()
    print(data)

assert file.closed


from collections import namedtuple

Task = namedtuple("Task", "task_id title urgency")

with open("tasks.txt") as file:
    for line in file:
        stripped_line = line.strip()
        task_id, title, urgency = stripped_line.split(",")
        task = Task(task_id, title, urgency)
        print(f"{stripped_line}: {task}")

desired_output = [
    '#1: 1001,Homework,5', 
    '#2: 1002,Laundry,3', 
    '#3: 1003,Grocery,4'
]


with open("tasks.txt") as file:
    lines = file.readlines()
    updated_lines = [f"#{row}: {line.strip()}" for row, line in enumerate(lines, start=1)]

assert desired_output == updated_lines



with open("tasks.txt") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))
    print(file.readline(8))
    print(file.readline())

data = """1001,Homework,5
1002,Laundry,3
1003,Grocery,4"""

with open("tasks_new.txt", "w") as file:
    print("File:", file)
    result = file.write(data)
    print("Writing result:", result)

with open("tasks_new.txt") as file:
    print("File:", file)
    result = file.write(data)
    print("Writing result:", result)

list_data = [
    '1001,Homework,5', 
    '1002,Laundry,3', 
    '1003,Grocery,4'
]

with open("tasks_list_write.txt", "w") as file:
    file.writelines(list_data)

with open("tasks_list_write.txt") as file:
    print(file.read())

new_task = "1004,Museum,3"
with open("tasks.txt", "a") as file:
    file.write(f"\n{new_task}")

#%% Solution:
list_data = [
    '1001,Homework,5', 
    '1002,Laundry,3', 
    '1003,Grocery,4'
]

updated_list_data = [f"{x}\n" for x in list_data]
with open("tasks_list_write.txt", "w") as file:
    file.writelines(updated_list_data)

with open("tasks_list_write.txt") as file:
    print(file.read())


#%% Section 11.2
import csv

with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    tasks_rows = list(csv_reader)
    print(tasks_rows)


with open("tasks.txt", newline="") as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)
    print("Field:", fields)
    for row in csv_reader:
        task_dict = dict(zip(fields, row))
        print(task_dict)


with open("tasks.txt", newline="") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

new_task = "1004,Museum,3"
with open("tasks.txt", "a", newline="") as file:
    file.write("\n")
    csv_writer = csv.writer(file)
    csv_writer.writerow(new_task.split(","))


 
tasks = [
    {'task_id': '1001', 'title': 'Homework', 'urgency': '5'},
    {'task_id': '1002', 'title': 'Laundry', 'urgency': '3'},
    {'task_id': '1003', 'title': 'Grocery', 'urgency': '4'}
]

fields = ['task_id', 'title', 'urgency']

with open("tasks_dict.txt", "w", newline="") as file:
    csv_writer = csv.DictWriter(file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(tasks)

# Solution

tasks = [
    ['1001', 'Homework', '5'],
    ['1002', 'Laundry', '3'],
    ['1003', 'Grocery', '4']
]

import csv

with open("tasks_writer.txt", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(tasks)

#%% Section 11.3
import pickle

task_tuple = (1001, "Homework", 5)
task_dict = {'task_id': '1002', 'title': 'Laundry', 'urgency': 3}

with open("task_tuple_saved.pickle", "wb") as file:
    pickle.dump(task_tuple, file)

with open("task_dict_saved.pickle", "wb") as file:
    pickle.dump(task_dict, file)


with open("task_tuple_saved.pickle", "rb") as file:
    task_tuple_loaded = pickle.load(file)

with open("task_dict_saved.pickle", "rb") as file:
    task_dict_loaded = pickle.load(file)

assert task_tuple == task_tuple_loaded
assert task_dict == task_dict_loaded


def doubler(x):
    return x * 2

doubler_pickle = pickle.dumps(doubler)
print(doubler_pickle)

doubler_loaded = pickle.loads(doubler_pickle)
assert doubler_loaded(5) == doubler(5)

import os
import pickle

class MaliciousTask:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def __reduce__(self):
        print("__reduce__ is called")
        return os.system, ('rm hacking.txt', )


malicious_task = MaliciousTask("Set fire", 5)

with open("test_malicious.pickle", "wb") as file:
    pickle.dump(malicious_task, file)

with open("test_malicious.pickle", "rb") as file:
    pickle.load(file)



pickle.dumps(os)
file = open("test_malicious.pickle", "rb")
pickle.dumps(file)

import os

class MaliciousTask:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def __reduce__(self):
        print("__reduce__ is called")
        return os.system, ('touch ./hacking.txt', )


#%% Section 11.4
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir()

assert data_folder.exists()

subject_ids = [123, 124, 125]
extensions = ["config", "dat", "txt"]
for subject_id in subject_ids:
    for extension in extensions:
        filename = f"subject_{subject_id}.{extension}"
        filepath = data_folder / filename
        with open(filepath, "w") as file:
            file.write(f"It's the file {filename}.")

data_folder = Path("data")

data_files = data_folder.glob("*.dat")
print("Data files:", data_files)

for data_file in data_files:
    print(f"Processing file: {data_file}")
    # applicable data processing steps here

data_files = data_folder.glob("*.dat")
for data_file in sorted(data_files):
    print(f"Processing file: {data_file}")
    # applicable data processing steps here

subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)
    
    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        _ = subject_file.rename(target_path)
        print(f"Moving {filename} to {target_path}")


import shutil

shutil.rmtree("subjects")

subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)
    
    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        _ = shutil.copy(subject_file, target_path)
        print(f"Copying {filename} to {target_path}")

Path("subjects").rmdir()


data_folder = Path("data")

for file in data_folder.glob("*.txt"):
    before = file.exists()
    file.unlink()
    after = file.exists()
    print(f"Deleting {file}, existing? {before} -> {after}")

# Solution
import shutil

shutil.rmtree("subjects")    

subject_ids = [123, 124, 125]
data_folder = Path("data")

for subject_id in subject_ids:
    subject_folder = Path(f"subjects/subject_{subject_id}")
    subject_folder.mkdir(parents=True, exist_ok=True)
    
    for subject_file in data_folder.glob(f"*{subject_id}*"):
        filename = subject_file.name
        target_path = subject_folder / filename
        if not target_path.exists():
            _ = shutil.copy(subject_file, target_path)
            print(f"Copying {filename} to {target_path}") 
        else:
            print(f"{filename} already exists at {target_path}") 


#%% Section 11.5
from pathlib import Path

subjects_folder = Path("subjects")

for dat_path in subjects_folder.glob("**/*.dat"):    #A

    subject_dir = dat_path.parent    #B

    filename = dat_path.stem     #C

    config_path = subject_dir / f"{filename}.config"

    print(f"{subject_dir} & {filename} -> {config_path}")

    dat_exists = dat_path.exists()
    config_exists = config_path.exists()

    with open(dat_path) as dat_file, open(config_path) as config_file:    #D
        print(f"Process {filename}: dat? {dat_exists}, config? {config_exists}\n")
        # process the subject's data

dat_path = Path("subjects/subject/subject_123.dat")
assert dat_path.suffix == ".dat"


def process_data_using_size_cutoff(min_size, max_size):
    data_folder = Path("data")
    for dat_path in data_folder.glob("*.dat"):
        filename = dat_path.name
        size = dat_path.stat().st_size
        if min_size < size < max_size: 
            print(f"{filename}, Good; {size},  within [{min_size}, {max_size}]")
        else:
            print(f"{filename}, Bad; {size}, outside [{min_size}, {max_size}]")

process_data_using_size_cutoff(20, 40)

process_data_using_size_cutoff(40, 60)

import time

subject_dat_path = Path("data/subject_123.dat")
created_time = subject_dat_path.stat().st_birthtime
readable_time = time.ctime(created_time)
print(f"Creation time: {created_time} -> {readable_time}")

modi_time = subject_dat_path.stat().st_mtime
print(f"Modification time: {time.ctime(modi_time)}")

from pathlib import Path
import time

def select_recent_files_24h(directory):
    dir_path = Path(directory)
    current_time = time.time()
    time_cutoff = current_time - 24 * 3600
    good_files = []
    for file_path in dir_path.glob("*"):
        file_time = file_path.stat().st_birthtime
        if time_cutoff <= file_time <= current_time:
            good_files.append(file_path)

    return good_files

