import json
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from task.models import Task, List
from user_account.models import UserAccount
from task.api.serializers import TaskSerializer, ListSerializer

class TaskApi(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = UserAccount.objects.create(username="user",
                                                password ="password")
        self.list = List.objects.create(user= self.user, title="list 01")
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_user_lists(self):
        response = self.client.get(reverse('todo_list_list'))
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_list(self):
        response = self.client.get(reverse('todo_list_rud',
                                            args=(str(self.list.id),)))
        serializer = ListSerializer(self.list, many=False)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_single_list(self):
        data = {
            'user': self.user.pk,
            'title': 'new list'
        }
        response = self.client.post(reverse('todo_list_create'),
                                            data=data,
                                            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_single_list(self):
        data = {
            'user': self.user.pk,
            'title': 'edit list'
        }
        response = self.client.put(reverse('todo_list_rud',
                                            args=(str(self.list.id),)),
                                            data=data,
                                            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_list(self):
        response = self.client.delete(reverse('todo_list_rud',
                                            args=(str(self.list.id),)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
