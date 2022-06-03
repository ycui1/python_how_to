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

create_task(inject_bug=True)