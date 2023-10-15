from django.test import TestCase
from users.forms import RegisterForm
from users.models import *

class TestRegister(TestCase):

    def test_register(self) -> None:
        data = {
            'username': 'rrrrrr',
            'password1': 'gglox445',
            'password2': 'gglox445',
            'email': 'rfjd@mail.ru',
            'bio': 'bio',
            'first_name': 'first',
            'last_name': 'last',
        }
        self.client.post('/registr/', data)
        self.assertTrue(InstaUser.objects.filter(username='rrrrrr').exists())

    def test_fail_register(self) -> None:
        data = {
            'username': 'rrrrrr',
            'password1': 'gglox445',
            'password2': '1',
            'email': 'rfjd@mail.ru',
            'bio': 'bio',
            'first_name': 'first',
            'last_name': 'last',
        }
        self.client.post('/registr/', data)
        self.assertFalse(InstaUser.objects.filter(username='rrrrrr').exists())