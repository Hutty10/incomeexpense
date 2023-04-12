from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase

from user.models import User


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.register_url = reverse("user:register")
        self.login_url = reverse("user:login")
        self.fake = Faker()
        self.user_data = {
            "email": self.fake.email(),
            "username": self.fake.email().split("@")[0],
            "password": self.fake.email(),
        }
        self.user = User.objects.create_user(
            email=self.user_data.get("email") + "m",
            username=self.user_data.get("username") + "m",
            password=self.user_data.get("password") + "m",
        )
        return super().setUp()

    def tearDown(self) -> None:
        self.user.delete()
        return super().tearDown()
