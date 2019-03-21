from django.urls import path, include

from rest_framework import routers
from . import viewsets

urlpatterns = [
    # LIST
    path('l/', viewsets.ListAPIViewSet.as_view(),
                name='todo_list_list'),
    path('lrud/<pk>', viewsets.ListRUDAPIViewSet.as_view(),
                name='todo_list_rud'),
    path('lc/', viewsets.CreateListAPIViewSet.as_view(),
                name='todo_list_create'),

    # TASK
    path('tc/', viewsets.CreateTaskAPIViewSet.as_view(),
                name='todo_task_create'),
    path('trud/<list_pk>/<pk>', viewsets.TaskRUDAPIViewSet.as_view(),
                name='todo_task_rud'),

]
