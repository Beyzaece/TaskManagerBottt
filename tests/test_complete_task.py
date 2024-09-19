import unittest
from database import add_task, complete_task, show_tasks

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        add_task('Görev tamamlanacak')

    def test_complete_task(self):
        tasks_before = show_tasks()
        task_id = tasks_before[-1][0]  # Son eklenen görev ID'si
        complete_task(task_id)
        tasks_after = show_tasks()
        self.assertTrue(any(task[0] == task_id and task[2] == 1 for task in tasks_after))

if __name__ == '__main__':
    unittest.main()
