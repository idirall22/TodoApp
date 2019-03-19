from rest_framework.viewsets import ModelViewSet
from .serializers import UserAccountSerializer
from ..models import UserAccount

class UserAccountViewSet(ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()
