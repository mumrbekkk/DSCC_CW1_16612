from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Project

User = get_user_model()

class ProjectModelTest(TestCase):
    url_names = [
        "project_list",
        "project_create",
        "project_detail",
        "project_update",
        "project_delete_confirmation",
    ]
    TEST_USERNAME = "test_user"
    TEST_PASSWORD = "123"
    TEST_PROJECT_NAME = "TestProject"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.TEST_USERNAME,
            password=self.TEST_PASSWORD
        )
        self.project = Project.objects.create(
            name=self.TEST_PROJECT_NAME,
            owner=self.user
        )

    def test_project_str(self):
        self.assertEqual(str(self.project), self.TEST_PROJECT_NAME)


    def test_project_create(self):
        self.assertEqual(self.project.name, self.TEST_PROJECT_NAME)

        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)

        self.client.post(
            reverse("project_create"),
            {"name": "New Project"}
        )

        self.assertEqual(Project.objects.count(), 2)
        self.assertTrue(Project.objects.filter(name="New Project").exists())

    def test_endpoint_access_without_auth_redirects(self):
        id_required_url_names = self.url_names[2:]
        id_not_required_url_names = self.url_names[:2]

        for url_name in id_not_required_url_names:
            response = self.client.get(reverse(url_name))
            self.assertEqual(response.status_code, 302)

        for url_name in id_required_url_names:
            response = self.client.get(reverse(url_name, args=[self.project.pk]))
            self.assertEqual(response.status_code, 302)

    def test_project_update(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)

        self.client.post(
            reverse("project_update", args=[self.project.pk]),
            {"name": "Updated"}
        )

        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Updated")

    def test_project_delete(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)

        self.client.post(
            reverse("project_delete", args=[self.project.pk])
        )

        self.assertEqual(Project.objects.count(), 0)




