from rest_framework import serializers
from ..models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meat:
        model = Task
        fields = ('id','description','created','finish','primary','done')