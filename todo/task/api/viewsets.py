from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import TaskSerializer
from ..models import Task

User_Account = get_user_model()

class TaskViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
