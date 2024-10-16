from django.test import TestCase


# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        Token.objects.create(user=self.user)

    def test_login_with_token(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_failed_login(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('detail', response.data)

    def test_logout(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)

    def test_protected_view(self):
        url = reverse('protected-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        # Login and try again
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(Token.objects.first().key))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)
