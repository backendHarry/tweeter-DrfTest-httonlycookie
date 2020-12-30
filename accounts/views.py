from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .serializers import RegisterSerializer, UserSerializer, LoginSerializer

from knox.models import AuthToken


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data},
        status=status.HTTP_201_CREATED
        )

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        myResponse = Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token},
        status=status.HTTP_200_OK
        )
        myResponse.set_cookie(key="token", value=token, httponly=True)
        return myResponse
