#####################################################################################
#
# 12.1	How do I monitor my program with logging?
#
#####################################################################################

#%%
import logging

logger_not_good = logging.Logger("task_app")

#%%
logger_good = logging.getLogger("task_app")

#%%
logger0 = logging.Logger("task_app")
logger1 = logging.Logger("task_app")
logger2 = logging.Logger("task_app")

assert logger0 is not logger1
assert logger1 is not logger2
assert logger0 is not logger2

#%%
logger0_good = logging.getLogger("task_app")
logger1_good = logging.getLogger("task_app")
logger2_good = logging.getLogger("task_app")

assert logger0_good is logger1_good is logger2_good

#%%
class Task:
    def __init__(self, title):
        self.title = title

    def remove_from_db(self):
        # add the task to the database
        task_removed = True
        return task_removed

task = Task("Laundry")
if task.remove_from_db():
    print(f"removed the task {task.title} from the database")

#%%
import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("taskier.log")

logger.addHandler(file_handler)

#%%
task = Task("Laundry")
if task.remove_from_db():
    logger.warning(f"removed the task {task.title} from the database")

#%%
def check_log_content(filename):
    with open(filename) as file:
        return file.read()

log_records = check_log_content("taskier.log")
print(log_records)

#%%
stream_handler = logging.StreamHandler()

logger.addHandler(stream_handler)

logger.warning("Just a random warning event.")

#%%
log_records = check_log_content("taskier.log")
print(log_records)

#####################################################################################
#
# 12.2	How do I categorize and format log records?
#
#####################################################################################
#%%
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

print(logger.level, logging._levelToName[logger.level])
print(logger.handlers)

# %%
def logging_messages_all_levels():
    logger.critical("--Critical message")
    logger.error("--Error message")
    logger.warning("--Warning message")
    logger.info("--Info message")
    logger.debug("--Debug message")

logging_messages_all_levels()

log_records = check_log_content("taskier.log")
print(log_records)

#%%
logger.setLevel(logging.DEBUG)

handler_warning = logging.FileHandler("taskier_warning.log")
handler_warning.setLevel(logging.WARNING)
logger.addHandler(handler_warning)

handler_critical = logging.FileHandler("taskier_critical.log")
handler_critical.setLevel(logging.CRITICAL)
logger.addHandler(handler_critical)

logging_messages_all_levels()

warning_log_records = check_log_content("taskier_warning.log")
print(warning_log_records)
# output the following lines:


critical_log_records = check_log_content("taskier_critical.log")
print(critical_log_records)

#%%
import logging

logger = logging.getLogger(__name__)    #A

formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s - %(message)s")   #B

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)    #C
logger.addHandler(stream_handler)

def log_some_records():
    logger.info("App is starting")
    logger.error("Failed to save the task to the db")
    logger.info("Created a task by the user")
    logger.critical("Can't update the status of the task")

log_some_records()


# %%
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s - %(message)s")

file_handler = logging.FileHandler("taskier.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#####################################################################################
#
# 12.3	How do I handle exceptions?
#
#####################################################################################
# %%
from collections import namedtuple
Task = namedtuple("Task", ["title", "urgency"])
task_text0 = "Laundry,3"

def process_task_string0(text):
    title, urgency_str = text.split(",")
    urgency = int(urgency_str)
    task = Task(title, urgency)
    return task

processed_task0 = process_task_string0(task_text0)
assert processed_task0 == Task(title='Laundry', urgency=3)


task_text1 = "Laudry,3#"
processed_task1 = process_task_string0(task_text1)

#%%
def process_task_string1(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except:
        print("Couldn't cast the number")
        return None
    task = Task(title, urgency)
    return task

#%%
processed_task1 = process_task_string1(task_text1)
# output: Encountered an exception

assert processed_task1 is None

#%%
processed_task0 = process_task_string1(task_text0)
assert processed_task0 == Task(title='Laundry', urgency=3)

#%%
def process_task_string2(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except:
        print("Couldn't cast the number")
        return None
    task = Task(title, urgency)
    return task

#%%
# expect error below
pending_task.urgency = 3

#%%
process_task_string2("Laundry,3")

#%%
def process_task_string3(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except ValueError:
        print("Couldn't cast the number")
        return None
    task = Task(title, urgency)
    return task

process_task_string3("Laundry,3#")

#%%
def process_task_string4(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except ValueError:
        print("Couldn't cast the number")
        return None
    except NameError:
        print("You're referencing an undefined name")
        return None
    task = Task(title, urgency)
    return task

process_task_string4("Laundry,3")

#%%
def process_task_string5(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        pending_task.urgency = urgency
    except (ValueError, NameError):
        print("Couldn't process the task string")
        return None
    task = Task(title, urgency)
    return task

process_task_string5("Laundry,3")

process_task_string5("Laundry,3#")

#%%
def process_task_string6(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    task = Task(title, urgency)
    return task


process_task_string6("Laundry,3#")

#####################################################################################
#
# 12.4	How do I use else and finally clauses in exception handling?
#
#####################################################################################
#%%
# part of the code taken from a previous snippet, don't expect to run
try:
    urgency = int(urgency_str)
except ValueError as ex:
    print(f"Couldn't cast the number. Description: {ex}")
    return None
task = Task(title, urgency)

#%%
def process_task_string7(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    else:
        task = Task(title, urgency)
        return task

processed_task7 = process_task_string7("Laundry,3")
assert processed_task7 == Task("Laundry", 3)

#%%
processed_task = process_task_string7("Laundry,3#")
print(processed_task)

#%%
def process_task_string8(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    else:
        task = Task(title, urgency)
        return task
    finally:
        print(f"Done processing text: {text}")

task_no_exception = process_task_string8("Laundry,3")
task_exception = process_task_string8("Laundry,3#")

#%%
def process_task_string9(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        task = Task(title, urgency)
        return task
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    finally:
        print(f"Done processing text: {text}")

task = process_task_string9("Laundry,3")
assert task == Task("Laundry", 3)

process_task_string9("Laundry,3#")

#%%
def process_task_challenge(text):
    title, urgency_str = text.split(",")
    try:
        urgency = int(urgency_str)
        task = Task(title, urgency)
        return task
    except ValueError as ex:
        print(f"Couldn't cast the number. Description: {ex}")
        return None
    finally:
        print(f"Done processing text: {text}")
        return "finally"

processed = process_task_challenge("Laundry,3")
print(processed)

#####################################################################################
#
# 12.5	How do I raise informative exceptions with custom exception classes?
#
#####################################################################################
#%%
# expect errors
int("3#")
1 / 0

#%%
raise ValueError

raise ZeroDivisionError

#%%
try:
    1 / 0
except ZeroDivisionError as ex:
    print(f"Type: {type(ex)}")
    print(f"Is an instance of ZeroDivisionError? {isinstance(ex, ZeroDivisionError)}")

#%%
raise ValueError("Please use the correct parameter.")

#%%
code_used = "3#"
raise ValueError(f"You used a wrong parameter: {code_used!r}")

#%%
class Task:
    def __init__(self, title):
        self.title = title

#%%
class Task:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("Please instantiate the Task using string as its title")

task = Task(100)

#%%
class TaskierError(Exception):
    pass


#%%
class FileExtensionError(TaskierError):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def __str__(self):
        return f"The file ({self.file_path}) doesn't appear to be a CSV file."

from pathlib import Path

def upload_file(file_path):
    path = Path(file_path)
    if path.suffix.lower() != ".csv":
        raise FileExtensionError(file_path)
    else:
        print(f"Processing the file at {file_path}")

#%%
def custom_upload_file(file_path):
    try:
        upload_file(file_path)
    except FileExtensionError as ex:
        print(ex)
    else:
        print("Custom upload file is done.")

custom_upload_file("tasks.csv")
custom_upload_file("tasks.docx")