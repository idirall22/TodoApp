import json
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from task.models import Task
from user_account.models import UserAccount
from task.api.serializers import TaskSerializer

class TaskApi(TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000'
        self.client = Client()

        self.user = UserAccount.objects.create(username="user", password ="password")
        self.task = Task.objects.create(user=self.user, description = "task 01")

    def test_get_tasks(self):
        response = self.client.get(reverse('task-list'))
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        task = Task.objects.first()
        response = self.client.get(reverse('task-list') + str(task.id) + '/')
        serializer = TaskSerializer(task, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_task(self):
        data = {
            'user': self.user.id,
            'description': 'simple desc'
        }
        response = self.client.post(reverse('task-list'),
                                json.dumps(data),
                                content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_task(self):
        data = {
            'user': self.user.id,
            'description': 'edited desc'
        }
        response = self.client.put(reverse('task-list') + str(self.task.id) + '/',
                                json.dumps(data),
                                content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-list') + str(self.task.id) + '/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
