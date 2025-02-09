from django.test import TestCase
from todo.models import Todo


class TodoModelTest(TestCase):
    def setUp(self):
        # Creating a Todo instance with the correct field name "title"
        self.todo = Todo.objects.create(title="Test Todo", description="This is a test", completed=False)

    def test_todo_creation(self):
        # Assert the title is correct
        self.assertEqual(self.todo.title, "Test Todo")
        # Assert that completed is False
        self.assertFalse(self.todo.completed)
