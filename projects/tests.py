from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()

class ProjectModelTest(TestCase):

    def test_project_creation(self):
        user = User.objects.create_user(username="testuser", password="123")
        project = Project.objects.create(name="Test", owner=user)
        self.assertEqual(project.name, "Test")