# from task_func import Task, create_task
# import unittest

# class TestTaskCreation(unittest.TestCase):
#     def test_create_task(self):
#         task_text = "Laundry,3"
#         created_task = create_task(task_text)
#         self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)


# if __name__ == "__main__":
#     unittest.main()

# from task_func import Task, create_task, create_task_from_dict
# import unittest

# class TestTaskCreation(unittest.TestCase):
#     def test_create_task(self):
#         task_text = "Laundry,3"
#         created_task = create_task(task_text)
#         self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)

#     def test_create_task_from_dict(self):
#         task_data = {"title": "Laundry", "urgency": 3}
#         created_task = create_task_from_dict(task_data)
#         self.assertEqual(created_task.__dict__, Task("Laundry", 3).__dict__)


# if __name__ == "__main__":
#     unittest.main()

from task_func import Task, create_task, create_task_from_dict
import unittest

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

if __name__ == "__main__":
    unittest.main()