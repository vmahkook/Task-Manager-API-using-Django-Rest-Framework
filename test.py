from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            status="TODO",
            priority="HIGH"
        )
        self.assertEqual(task.title, "Test Task")
