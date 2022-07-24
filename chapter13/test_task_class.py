from task_class import Task
import unittest

class TestTask(unittest.TestCase):
    def setUp(self):
        task_to_compare = Task("Laundry", 3)
        self.task_dict = task_to_compare.__dict__

    def test_create_task_from_text(self):
        task_text = "Laundry,3"
        created_task = Task.task_from_text(task_text)
        self.assertEqual(created_task.__dict__, self.task_dict)

    def test_create_task_from_dict(self):
        task_data = {"title": "Laundry", "urgency": 3}
        created_task = Task.task_from_dict(task_data)
        self.assertEqual(created_task.__dict__, self.task_dict)
    
    def test_formatted_display(self):
        task = Task("Laundry", 3)
        displayed_text = task.formatted_display()
        self.assertEqual(displayed_text, "Laundry(3)")

if __name__ == "__main__":
    unittest.main()