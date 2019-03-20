from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import UserAccountSerializer
from ..models import UserAccount

class UserAccountViewSet(ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token = Token.objects.get()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
