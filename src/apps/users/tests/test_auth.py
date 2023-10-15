from django.test import TestCase
from apps.users.models import *

class TestAuth(TestCase):

    def setUp(self) -> None:
        self.user = InstaUser.objects.create_user(
            username='testuser',
            password='password',
        )

    def test_auth(self) -> None:
        self.assertTrue(self.client.login(username='testuser', password='password'))
    
    def test_not_auth(self) -> None:
        self.assertFalse(self.client.login(username='testuser1', password='password'))