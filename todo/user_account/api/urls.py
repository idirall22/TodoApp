from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, re_path

from .viewsets import UserAccountViewSet

router = routers.SimpleRouter()
router.register(r'user', UserAccountViewSet)

urlpatterns = router.urls
