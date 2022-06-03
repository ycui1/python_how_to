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