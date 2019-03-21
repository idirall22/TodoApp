from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import TaskSerializer, ListSerializer
from ..models import Task, List

User_Account = get_user_model()

class PermissionOwner():
    """ This permission allow the user to edit update or delete only
    his Lists or Tasks"""

    def get_object(self):
        if 'list_pk' in self.kwargs:
            list = List.objects.get(pk=self.kwargs['list_pk'])
            instance = self.model.objects.get(pk=self.kwargs['pk'])
            if list.user != self.request.user:
                raise PermissionDenied(
                {'message':'You don\'t have permission to access'})
            return instance
        else:
            instance = self.model.objects.get(pk=self.kwargs['pk'])
            if instance.user != self.request.user:
                raise PermissionDenied(
                {'message':'You don\'t have permission to access'})
            return instance

# LIST ****************************************************

class ListAPIViewSet(generics.ListAPIView):
    """ Retrive Lists of a User Authenticated """

    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)

class ListRUDAPIViewSet(generics.RetrieveUpdateDestroyAPIView):
    """ User Authenticated can delete, update, and retrive
        single list"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer
    model = List

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)

class CreateListAPIViewSet(generics.CreateAPIView):
    """ User Authenticated can create list """

    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

# TASK ****************************************************


class TaskRUDAPIViewSet(PermissionOwner, generics.RetrieveUpdateDestroyAPIView):
    """ User Authenticated can delete, update, and retrive
        single task"""

    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    model = Task

    def get_queryset(self):
        return self.model.objects.get(pk=self.kwargs['pk'])

class CreateTaskAPIViewSet(generics.CreateAPIView):
    """ User Authenticated can create task """

    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        list_id = request.data.pop('list_id')
        list = List.objects.get(pk=list_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        list.tasks.add(task)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)
