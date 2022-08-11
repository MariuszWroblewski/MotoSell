from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
# Create your views here.


class CreateUser(generics.CreateAPIView):
    """
    Create a new user.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer
    name = 'create-user'


class LogoutUser(generics.GenericAPIView):
    """
    Logout.
    permissions - isAuthenticated
    """

    permission_classes = [permissions.IsAuthenticated]
    name = 'logout-user'

    def post(self, request):
        try:
            refresh_token = request.data('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
