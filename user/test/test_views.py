from django.test import override_settings

from ..models import User
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data["email"], self.user_data["email"])
        self.assertEqual(res.data["username"], self.user_data["username"])
        self.assertEqual(res.status_code, 201)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data["email"]
        user = User.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        # import pdb
        res = self.client.post(self.login_url, self.user_data, format="json")
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)