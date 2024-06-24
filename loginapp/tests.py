# Create your tests here.
from django.test import TestCase, Client

class LoginTestCase(TestCase):

    def test_valid_login(self):
        client = Client()
        response = client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.json())

    def test_invalid_login(self):
        client = Client()
        response = client.post('/login/', {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertNotIn('email', response.json())