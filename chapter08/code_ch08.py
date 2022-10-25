#####################################################################################
#
# 8.1	How do I define the initialization method for a class?
#
#####################################################################################
#%%
class Task:
    def __init__(self):
        print("Creating an instance of Task class")


task = Task()
# output: Creating an instance of Task class

#%%
class Task:
    def __init__(self):
        print(f"Memory address (self): {id(self)}")

task = Task()
# output: Memory address (self): 140702458470768

task_address = f"Memory address (task): {id(task)}"
print(task_address)
# output: Memory address (task): 140702458470768   #A

#%%
class Task:
    def __init__(self):
        print(f"__init__ gets called, creating object at {id(self)}")

    def __new__(cls):
        new_task = object.__new__(cls)
        print(f"__new__ gets called, creating object at {id(new_task)}")
        return new_task


task = Task()



#%%
task = Task.__new__(Task)
# output: __new__ gets called, creating object at 140702458476192


Task.__init__(task)
# output: __init__ gets called, creating object at 140702458476192

#%%
# Expect the first two assignments to fail
def = 5
# ERROR: SyntaxError: invalid syntax

class = 7
# ERROR: SyntaxError: invalid syntax

self = 9
# Works!

#%%
import keyword

words_to_check = ["def", "class", "self", "lambda"]
for word in words_to_check:
    print(f"Is {word:^8} a keyword? {keyword.iskeyword(word)}")

#%%
class Task:
    def __init__(this):
        print("An instance is created with this instead of self.")

task = Task()
# output: An instance is created with this instead of self.


#%%
from collections import namedtuple

Task = namedtuple("Task", "title desc urgency")

task = Task("Laundry", "Wash clothes", 3)

print(task)
# output: Task(title='Laundry', desc='Wash clothes', urgency=3)

#%%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency


#%%
task = Task("Laundry", "Wash clothes", 3)

#%%
print(task.__dict__)
# output: {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}


#%%
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


#%%
task = Task("Laundry", "Wash clothes", 3)
print(task.status)

# ERROR: AttributeError: 'Task' object has no attribute 'status'

task.complete()
print(task.status)
# output: completed


#%%
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


#%%
task = Task("Laundry", "Wash clothes", 3)
print(task.__dict__)
# output: {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3, 'status': 'created', 'tags': []}


#%%
def __init__(self, title, desc, urgency, user):
    self.title = title
    self.desc = desc
    self.urgency = urgency
    self.user = user


#%%
class Task:
    user = "the logged in user"
    
    def __init__(self, title, desc, urgency):
        pass

#####################################################################################
#
# 8.2	When do I define instance, static, and class methods?
#
#####################################################################################
class Task:
    # __init__ stays the same as before

    def complete(self):
        print(f"Memory Address (self): {id(self)}")
        self.status = "completed"


task = Task("Laundry", "Wash clothes", 3)
task.complete()
# output: Memory Address (self): 140508514865536


task_id = f"Memory Address (task): {id(task)}"
print(task_id)
# output: Memory Address (task): 140508514865536


#%%
from datetime import datetime

class Task:
    @staticmethod
    def get_timestamp():
        now = datetime.now()
        timestamp = now.strftime("%b %d %Y, %H:%M")
        return timestamp


#%%
refresh_time = f"Data Refreshed: {Task.get_timestamp()}"

print(refresh_time)
# output: Data Refreshed: Mar 04 2022, 15:43


#%%
task_dict = {"title": "Laundry", "desc": "Wash clothes", "urgency": 3}

#%%
task = Task(task_dict["title"], task_dict["desc"], task_dict["urgency"])

#%%
class Task:
    # __init__ stays the same as before

    @classmethod
    def task_from_dict(cls, task_dict):
        title = task_dict["title"]
        desc = task_dict["desc"]
        urgency = task_dict["urgency"]
        task_obj = cls(title, desc, urgency)
        return task_obj


#%%
task = Task.task_from_dict(task_dict)

print(task.__dict__)
# output: {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3, 'status': 'created', 'tags': []}

#####################################################################################
#
# 8.3	How do I apply finer access control to a class?
#
#####################################################################################
#%%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"
        self.note = ""

    def complete(self, note = ""):
        self.status = "completed"
        self.note = self.format_note(note)
        
    def format_note(self, note):
        formatted_note = note.title()
        return formatted_note


#%%
task.__format_note("a note")
# ERROR: AttributeError: 'Task' object has no attribute '__format_note'.


#%%
task._Task__format_note("a note")
# output: 'A Note'

#%%
print(task.status)
# output: created

task.status = "completed"
print(task.status)
# output: completed

#%%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"

    @property
    def status(self):
        return self._status

    def complete(self):
        self._status = "completed"


#%%
task = Task("Laundry", "Wash clothes", 3)

print(task.status)
# output: created


#%%
task.status = "completed"
# ERROR: AttributeError: can't set attribute 'status'


#%%
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
            print(f"invalid status: {value}")    #A



#%%
task = Task("Laundry", "Wash clothes", 3)
task.status = "completed"
# output: task status set to completed

task.status = "random"
# output: invalid status: random

#####################################################################################
#
# 8.4	How do I customize string representation for a class?
#
#####################################################################################
#%%
print(task)
# output: <__main__.Task object at 0x7f9f280d6800>


#%%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"


#%%
task = Task("Laundry", "Wash clothes", 3) 
print(task)
# output: Laundry: Wash clothes, urgency level 3


#%%
planned_task = f"Next Task - {task}"

print(planned_task)
# output: Next Task - Laundry: Wash clothes, urgency level 3


#%%
str(task)
# output: Laundry: Wash clothes, urgency level 3

#%%
planned_task

#%%
task

#%%
class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency

    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"

    def __repr__(self):
        return f"Task({self.title!r}, {self.desc!r}, {self.urgency})"    #A


#%%
task = Task("Laundry", "Wash clothes", 3)
task

#%%
repr(task)

#%%
task = Task("Laundry", "Wash clothes", 3)

task_repr = repr(task)

task_repr_eval = eval(task_repr)

print(type(task_repr_eval))
# output: <class '__main__.Task'>

print(task_repr_eval)
# output: Laundry: Wash clothes, urgency level 3


#%%
class Task:
    # __init__ and __str__ stay the same

    def __repr__(self):
        return f"Task({self.title}, {self.desc}, {self.urgency})"


task = Task("Laundry", "Wash clothes", 3)

print(repr(task))
# output: Task(Laundry, Wash clothes, 3)


#%%
# Expect the code to fail
eval(repr(task))


#####################################################################################
#
# 8.5	Why and how do I create a superclass and subclasses?
#
#####################################################################################
#%%
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def login(self):
        print(f"An employee {self.name} just logged in.")

    def logout(self):
        print(f"An employee {self.name} just logged out.")


class Supervisor(Employee):
    pass


#%%
supervisor = Supervisor("John", "1001")

print(supervisor.name)
# output: John

supervisor.login()
# output: An employee John just logged in.


#%%
class Supervisor(Employee):
    def login(self):
        print(f"A supervisor {self.name} just logged in.")

#%%
supervisor = Supervisor("John", "1001")

supervisor.login()
# output: A supervisor John just logged in.


#%%
Supervisor.mro()

#%%
class Supervisor(Employee):
    def logout(self):
        super().logout()
        print("Additional logout actions for a supervisor")


#%%
supervisor = Supervisor("John", "1001")

supervisor.logout()


#%%
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def _request_vacation(self):
        print("Send a vacation request to the employee's supervisor.")

    def __transfer_group(self):
        print("Transfer the employee to a different group.")

#%%
class Supervisor(Employee):
    def do_something(self):
        self._request_vacation()
        self.__transfer_group()


#%%
supervisor = Supervisor("John", "1001")
supervisor.do_something()