from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class AuthTest(TestCase):
    TEST_USERNAME = "test_user"
    TEST_PASSWORD = "123"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.TEST_USERNAME,
            password=self.TEST_PASSWORD
        )

    def test_authenticated_user_can_access_list(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)
        response = self.client.get(reverse("project_list"))
        self.assertEqual(response.status_code, 200)