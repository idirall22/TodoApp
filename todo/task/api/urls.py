from django.urls import path, include

from rest_framework import routers
from . import viewsets

urlpatterns = [
    # LIST
    path('l/', viewsets.ListAPIViewSet.as_view(),
                name='todo_list_list'),
    path('ld/<pk>', viewsets.ListDetailAPIViewSet.as_view(),
                name='todo_list_detail'),
    path('lc/', viewsets.CreateListAPIViewSet.as_view(),
                name='todo_list_create'),
    path('lu/<pk>', viewsets.UpdateListAPIViewSet.as_view(),
                name='todo_list_update'),
    path('lde/<pk>', viewsets.DestroyListAPIViewSet.as_view(),
                name='todo_list_Delete'),
    # TASK
    path('td/', viewsets.TaskDetailAPIViewSet.as_view(),
                name='todo_list_detail'),
    path('tc/', viewsets.CreateTaskAPIViewSet.as_view(),
                name='todo_list_create'),
    path('tu/<pk>', viewsets.UpdateTaskAPIViewSet.as_view(),
                name='todo_list_update'),
    path('td/<pk>', viewsets.DestroyTaskAPIViewSet.as_view(),
                name='todo_list_Delete'),
]
