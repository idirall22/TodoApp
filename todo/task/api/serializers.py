from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Task

User_Account = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','user','description','created','finish','primary','done')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        task = Task(
                user=validated_data['user'],
                description=validated_data['description']
                )
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.finish = validated_data.get('finish', instance.finish)
        instance.primary = validated_data.get('primary', instance.primary)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
