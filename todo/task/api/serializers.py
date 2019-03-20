from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Task, List

User_Account = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        task = Task(description=validated_data['description'])
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.finish = validated_data.get('finish', instance.finish)
        instance.primary = validated_data.get('primary', instance.primary)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance

class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = ('id','user','title', 'tasks')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        list = List(
                user=validated_data['user'],
                title=validated_data['title']
                )
        list.save()
        return list

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
