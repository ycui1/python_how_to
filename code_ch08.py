class Task:
    def __init__(self):
        print("Creating an instance of Task class")

task = Task()


class Task:
    def __init__(self):
        print(f"Memory address (self): {id(self)}")

task = Task()

task_address = f"Memory address (task): {id(task)}"
print(task_address)

class Task:
    def __init__(self):
        print(f"__init__ gets called, creating object at {id(self)}")

    def __new__(cls):
        new_task = object.__new__(cls)
        print(f"__new__ gets called, creating object at {id(new_task)}")
        return new_task


task = Task()


task = Task.__new__(Task)

Task.__init__(task)

def = 5
class = 7
self = 9

import imp
import keyword

words_to_check = ["def", "class", "self", "lambda"]
for word in words_to_check:
    print(f"Is {word:^8} a keyword? {keyword.iskeyword(word)}")


class Task:
    def __init__(this):
        print("An instance is created with this instead of self")

task = Task()

from collections import namedtuple

Task = namedtuple("Task", "title desc urgency")

task = Task("Laundry", "Wash clothes", 3)


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency


task = Task("Laundry", "Wash clothes", 3)

task.__dict__


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def complete(self):
        self.status = "completed"

    def add_tag(self, tag):
        if not self.tags:
            self.tags = []
        self.tags.append(tag)


task = Task("Laundry", "Wash clothes", 3)
print(task.status)

task.complete()
print(task.status)

class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []

    def complete(self):
        self.status = "completed"

    def add_tag(self, tag):
        self.tags.append(tag)

task = Task("Laundry", "Wash clothes", 3)
print(task.__dict__)



class Task:
    def __init__(self, title, desc, urgency, tags=[]):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = tags

    def add_tag(self, tag):
        self.tags.append(tag)

task0 = Task("Laundry", "Wash clothes", 3)
task1 = Task("Meseum", "Egypt exhibit", 4)

task0.add_tag("Housekeeping")
task1.tags

class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []

    def complete(self):
        print(f"Memory Address (self): {id(self)}")
        self.status = "completed"


task = Task("Laundry", "Wash clothes", 3)
task.complete()

task_id = f"Memory Address (task): {id(task)}"
print(task_id)


from datetime import datetime

class Task:
    @staticmethod
    def get_timestamp():
        now = datetime.now()
        timestamp = now.strftime("%b %d %Y, %H:%M")
        return timestamp

refresh_time = f"Data Refreshed: {Task.get_timestamp()}"
print(refresh_time)

task_dict = {"title": "Laundry", "desc": "Wash clothes", "urgency": 3}

task = Task(task_dict["title"], task_dict["desc"], task_dict["urgency"])

class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []

    @classmethod
    def task_from_dict(cls, task_dict):
        title = task_dict["title"]
        desc = task_dict["desc"]
        urgency = task_dict["urgency"]
        task_obj = cls(title, desc, urgency)
        return task_obj

task = Task.task_from_dict(task_dict)
print(task.__dict__)

class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []

    def complete(self, note = ""):
        self.status = "completed"
        self.note = self.format_note(note)
        
    def format_note(self, note):
        formatted_note = note.title()
        return formatted_note


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.status = "created"
        self.tags = []
        self.note = ""

    def _format_note(self, note):
        formatted_note = note.title()
        return formatted_note

    def __format_note(self, note):
        formatted_note = note.title()
        return formatted_note

    def complete(self, note=""):
        self.status = "completed"
        self.note = self.__format_note(note)


task = Task("Laundry", "Wash clothes", 3)
task._format_note("a note")

task.__format_note("a note")

task._Task__format_note("a note")

print(task.status)
task.status = "suspended"
print(task.status)


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed_values = ["created", "started", "completed", "suspended"]
        if value in allowed_values:
            self._status = value
            print(f"task status set to {value}")
        else:
            print(f"invalid status: {value}")




task = Task("Laundry", "Wash clothes", 3)

task.status = "completed"

task.status = "random"

print(task)


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.urgency})"

task = Task("Laundry", "Wash clothes", 3)
print(task)

planned_task = f"Next Task - {task}"
print(planned_task)

task

Task.__str__(task)

task = Task("Laundry", "Wash clothes", 3)

task_repr = repr(task)

task_repr_eval = eval(task_repr)

print(type(task_repr_eval))
# output:


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"

    def __repr__(self):
        return f"Task({self.title}, {self.desc}, {self.urgency})"


task = Task("Laundry", "Wash clothes", 3)
print(repr(task))

eval(repr(task))

task.__class__.__name__


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def login(self):
        print(f"An employee {self.name} just logged in.")


class Supervisor(Employee):
    pass


supervisor = Supervisor("John", "1001")
print(supervisor.name)

supervisor.login()

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def login(self):
        print(f"An employee {self.name} just logged in.")

    def logout(self):
        print(f"An employee {self.name} just logged out.")

class Supervisor(Employee):
    def login(self):
        print(f"A supervisor {self.name} just logged in.")

    def logout(self):
        super().logout()
        print("Additional logout actions for a supervisor")


supervisor = Supervisor("John", "1001")
supervisor.login()

Supervisor.mro()

supervisor = Supervisor("John", "1001")
supervisor.logout()


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def _request_vacation(self):
        print("Send a vacation request to the employee's supervisor.")

    def __transfer_group(self):
        print("Transfer the employee to a different group.")

    def test(self):
        self._request_vacation()
        self.__transfer_group()


class Supervisor(Employee):
    def do_something(self):
        self._request_vacation()
        self.__transfer_group()


supervisor = Supervisor("John", "1001")
supervisor.do_something()


class A:
    def __init__(self, a):
        pass


class B(A):
    def __init__(self, b, c):
        pass

B(1, 2)

