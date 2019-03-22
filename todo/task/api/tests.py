import json
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from task.models import Task, List
from user_account.models import UserAccount
from task.api.serializers import TaskSerializer, ListSerializer

class TaskApi(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.other_client = APIClient()

        self.user = UserAccount.objects.create(username="user",
                                                password ="password")
        self.other_user = UserAccount.objects.create(username="user2",
                                                password ="password")
        self.list = List.objects.create(user= self.user, title="list 01")
        self.task = Task.objects.create(description='task 01')
        self.list.tasks.add(self.task)
        self.token = Token.objects.get(user=self.user)
        self.other_token = Token.objects.get(user=self.other_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.other_client.credentials(HTTP_AUTHORIZATION='Token ' + self.other_token.key)

    def test_get_user_lists(self):
        response = self.client.get(reverse('todo_list_list'))
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_list(self):
        response = self.client.get(reverse('todo_list_rud',
                                    args=(self.list.id,)))
        bad_response = self.other_client.get(reverse('todo_list_rud',
                                    args=(self.list.id,)))

        serializer = ListSerializer(self.list, many=False)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
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
        bad_response = self.other_client.put(reverse('todo_list_rud',
                                            args=(str(self.list.id),)),
                                            data=data,
                                            format='json')

        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_list(self):
        bad_response = self.other_client.delete(reverse('todo_list_rud',
                                            args=(str(self.list.id),)))
        response = self.client.delete(reverse('todo_list_rud',
                                            args=(str(self.list.id),)))

        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # TASK

    def test_get_single_task(self):
        response = self.client.get(reverse('todo_task_rud',
                                    args=(self.list.id, self.task.id)))
        bad_response = self.other_client.get(reverse('todo_task_rud',
                                    args=(self.list.id, self.task.id)))

        serializer = TaskSerializer(self.task, many=False)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_single_task(self):
        data = {
            'list_id': self.list.id,
            'description': 'New task'
        }
        response = self.client.post(reverse('todo_task_create'),
                                            data=data,
                                            format='json')

        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_single_task(self):
        data = {
            'list_id': self.list.id,
            'description': 'edit task'
            }
        response = self.client.put(reverse('todo_task_rud',
                                            args=(self.list.id, self.task.id)),
                                            data=data,
                                            format='json')

        bad_response = self.other_client.put(reverse('todo_task_rud',
                                            args=(self.list.id, self.task.id)),
                                            data=data,
                                            format='json')

        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_task(self):
        bad_response = self.other_client.delete(reverse('todo_task_rud',
                                            args=(self.list.id, self.task.id)))
        response = self.client.delete(reverse('todo_task_rud',
                                            args=(self.list.id, self.task.id)))

        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
