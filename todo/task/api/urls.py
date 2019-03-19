from rest_framework import routers
from .viewsets import TaskViewSet

router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)

urlpatterns = router.urls
