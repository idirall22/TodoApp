import uuid
from django.db import models
from django.conf import settings

class Task(models.Model):
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    description = models.TextField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField(blank=True, null=True)
    primary = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

class List(models.Model):
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    tasks = models.ManyToManyField(Task, blank=True)
