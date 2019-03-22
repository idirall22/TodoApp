from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import UserAccountSerializer
from ..models import UserAccount

class RegisterUserAccountViewSet(generics.CreateAPIView):
    serializer_class = UserAccountSerializer
