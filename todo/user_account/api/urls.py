from rest_framework import routers
from .viewsets import UserAccountViewSet

router = routers.SimpleRouter()
router.register(r'user', UserAccountViewSet)

urlpatterns = router.urls
