import unittest
from database import add_task, delete_task, show_tasks

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        add_task('Görev silinecek')

    def test_delete_task(self):
        tasks_before = show_tasks()
        task_id = tasks_before[-1][0]  # Son eklenen görev ID'si
        delete_task(task_id)
        tasks_after = show_tasks()
        self.assertNotIn(task_id, [task[0] for task in tasks_after])

if __name__ == '__main__':
    unittest.main()
