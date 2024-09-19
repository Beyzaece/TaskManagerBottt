import unittest
from database import add_task, show_tasks
import sqlite3
class TestShowTasks(unittest.TestCase):
    def setUp(self):
        clear_db()
        add_task('Görev 1')
        add_task('Görev 2')

    def test_show_tasks(self):
        tasks = show_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn('Görev 1', [task[1] for task in tasks])
        self.assertIn('Görev 2', [task[1] for task in tasks])


def clear_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks')  # Tüm görevleri sil
    conn.commit()
    conn.close()
if __name__ == '__main__':
    unittest.main()
