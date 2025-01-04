# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserAuthTests(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('user_auth:register'), {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'Test',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('user_auth:authenticate_user'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertRedirects(response, reverse('user_auth:show_user'))

    def test_vote_restriction(self):
        response = self.client.get(reverse('polls:vote', args=(1,)))
        self.assertRedirects(response, '/user_auth/login/')
