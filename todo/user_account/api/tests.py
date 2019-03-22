from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from user_account.models import UserAccount
from rest_framework import status

class TestAPIUserAccount(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data={
            'username':'test',
            'email':'email@gmail.com',
            'password':'password'
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
