from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import TaskSerializer, ListSerializer
from ..models import Task, List

User_Account = get_user_model()

class ListAPIViewSet(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        return List.objects.all()

class ListDetailAPIViewSet(generics.RetrieveAPIView):
    serializer_class = ListSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])

class CreateListAPIViewSet(generics.CreateAPIView):
    serializer_class = ListSerializer

class UpdateListAPIViewSet(generics.UpdateAPIView):
    serializer_class = ListSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])

class DestroyListAPIViewSet(generics.DestroyAPIView):
    serializer_class = ListSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])

class TaskDetailAPIViewSet(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])

class CreateTaskAPIViewSet(generics.CreateAPIView):
    serializer_class = TaskSerializer

class UpdateTaskAPIViewSet(generics.UpdateAPIView):
    serializer_class = TaskSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])

class DestroyTaskAPIViewSet(generics.DestroyAPIView):
    serializer_class = TaskSerializer

    def get_object(self):
        return List.objects.get(pk=self.kwargs['pk'])
