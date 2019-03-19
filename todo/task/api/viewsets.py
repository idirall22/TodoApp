from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from ..models import Task

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
