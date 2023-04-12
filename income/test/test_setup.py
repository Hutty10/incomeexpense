from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from faker import Faker
from user.models import User
from ..models import Income


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.listCreate = reverse("income:incomes")
        self.detail = reverse("income:income", args=(1,))
        # print(self.detail)
        self.fake = Faker()
        self.user = User.objects.create_user(
            email=self.fake.email(),
            username=self.fake.email().split("@")[0],
            password=self.fake.email(),
            is_verified=True,
            is_active=True,
        )
        self.user2 = User.objects.create_user(
            email=self.fake.email() + "m",
            username=self.fake.email().split("@")[0] + "m",
            password=self.fake.email(),
            is_verified=True,
            is_active=True,
        )
        token = self.user.tokens().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        self.income_data = {
            # "id": 2,
            "source": "SALARY",
            "amount": 33,
            "description": "urururur",
            # "owner": self.user,
            "date": "2023-04-15",
        }
        self.income = Income.objects.create(
            source="SALARY",
            amount=33,
            description="urururur",
            owner=self.user,
            date="2023-04-15",
        )
        return super().setUp()

    def tearDown(self) -> None:
        self.user.delete()
        return super().tearDown()
