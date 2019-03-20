from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import TaskSerializer, ListSerializer
from ..models import Task, List

User_Account = get_user_model()

# LIST
class PermissionOwner():
    def get_object(self):
        instance = self.model.objects.get(pk=self.kwargs['pk'])
        if instance.user != self.request.user:
            raise PermissionDenied(
            {'message':'You don\'t have permission to access'})
        return instance

class ListAPIViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)

class ListRUDAPIViewSet(PermissionOwner,
                        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListSerializer
    model = List

class CreateListAPIViewSet(generics.CreateAPIView):
    serializer_class = ListSerializer

# TASK

class TaskRUDAPIViewSet(PermissionOwner,
                        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListSerializer
    model = Task

class CreateTaskAPIViewSet(generics.CreateAPIView):
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
