from rest_framework.test import force_authenticate, APIClient
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_cannot_create_income_without_loggin(self) -> None:
        # import pdb
        self.client.credentials()
        res = self.client.post(self.listCreate, self.income_data, format="json")
        # pdb.set_trace()
        self.assertEqual(res.status_code, 401)

    def test_user_can_create_successfully(self) -> None:
        res = self.client.post(self.listCreate, self.income_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_list_income_without_login(self) -> None:
        self.client.credentials()
        res = self.client.get(self.listCreate, format="json")
        self.assertEqual(res.status_code, 401)

    def test_user_can_list_income_after_login(self) -> None:
        res = self.client.get(self.listCreate, format="json")
        self.assertEqual(res.status_code, 200)

    def test_user2_cannot_get_user1_data(self) -> None:
        # import pdb
        token = self.user2.tokens().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        res = self.client.get(self.detail)
        # pdb.set_trace()
        self.assertEqual(res.status_code, 404)

    def test_user_can_get_income_detail(self) -> None:
        res = self.client.get(self.detail)
        self.assertEqual(res.status_code, 200)

    def test_user_can_delete_income(self) -> None:
        res = self.client.delete(self.detail)
        self.assertEqual(res.status_code, 204)
