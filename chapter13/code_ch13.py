#####################################################################################
#
# 13.1	How do I spot issues with tracebacks?
#
#####################################################################################
#%%
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def _update_db(self):
        # update the record in the database
        print("update the database")
        
    def update_urgency(self, urgency):
        self.urgency = urgency
        self._update_db()


task = Task("Laundry", 3)
task.update_urgency(4)


#####################################################################################
#
# 13.2	How do I debug my program interactively?
#
#####################################################################################
#%%
def create_task():
    import pdb; pdb.set_trace()

create_task()

#%%
def create_task():
    breakpoint()

create_task()

#%%
from collections import namedtuple
Task = namedtuple("Task", "title urgency")

def obtain_text_data(want_bad):
    text = "Laundry,3#" if want_bad else "Laundry,3"
    return text

def create_task(inject_bug: bool):
    breakpoint()
    task_text = obtain_text_data(inject_bug)
    title, urgency_text = task_text.split(",")
    urgency = int(urgency_text)
    task = Task(title, urgency)
    return task

#%%
create_task(inject_bug=False)

#####################################################################################
#
# 13.3	How do I test my functions automatically?
#
#####################################################################################
#%%
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency


def create_task(text):
    title, urgency_text = text.split(",")
    urgency = int(urgency_text)
    task = Task(title, urgency)
    return task

#%%
assert create_task("Laundry,3").__dict__ == Task("Laundry", 3).__dict__

#%%
from task_func import Task, create_task
import unittest

class TestTaskCreation(unittest.TestCase):
    def test_create_task(self):
        task_text = "Laundry,3"
        created_task = create_task(task_text)
        self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)

unittest.main()


#%%
def create_task_from_dict(task_data):
    title = task_data["title"]
    urgency = task_data["urgency"]
    task = Task(title, urgency)
    return task
    
#%%
class TestTaskCreation(unittest.TestCase):
    def test_create_task(self):
        task_text = "Laundry,3"
        created_task = create_task(task_text)
        self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)

    def test_create_task_from_dict(self):
        task_data = {"title": "Laundry", "urgency": 3}
        created_task = create_task_from_dict(task_data)
        self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)

#%%
unittest.main()

#%%
class TestTaskCreation(unittest.TestCase):
    def setUp(self):
        task_to_compare = Task("Laundry", 3)
        self.task_dict = task_to_compare.__dict__

    def test_create_task(self):
        task_text = "Laundry,3"
        created_task = create_task(task_text)
        self.assertEqual(created_task.__dict__, self.task_dict)

    def test_create_task_from_dict(self):
        task_data = {"title": "Laundry", "urgency": 3}
        created_task = create_task_from_dict(task_data)
        self.assertEqual(created_task.__dict__, self.task_dict)

#####################################################################################
#
# 13.4	How do I test a class automatically?
#
#####################################################################################
class Task:
    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency

    def formatted_display(self):
        displayed_text = f"{self.title} ({self.urgency})"
        raise TypeError()
        return displayed_text 