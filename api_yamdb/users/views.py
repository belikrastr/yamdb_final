from api import permissions
from api.serializers import (ForAdminSerializer, ForUserSerializer,
                             TokenSerializer)
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import DEFAULT_FROM_EMAIL

from .models import User


def create_confirmation_code_and_send_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Confirmation code',
        message=f'Your confirmation code {confirmation_code}',
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[user.email])


class APISignUp(APIView):
    """Регистрация пользователя"""
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = ForUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            create_confirmation_code_and_send_email(
                serializer.data['username'])
            return Response(
                {'email': serializer.data['email'],
                 'username': serializer.data['username']},
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class APIToken(APIView):
    """Получение токена"""
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_object_or_404(
                User, username=serializer.data['username']
            )
            confirmation_code = serializer.validated_data['confirmation_code']
            if default_token_generator.check_token(serializer.data['username'],
                                                   confirmation_code):
                token = AccessToken.for_user(user)
                return Response(
                    {'token': str(token)}, status=status.HTTP_200_OK)
        return Response({
            'confirmation code': 'Некорректный код подтверждения!'},
            status=status.HTTP_400_BAD_REQUEST)


class APIUser(APIView):
    """Работа с данными пользователя"""
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        serializer = ForUserSerializer(user, many=False)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        serializer = ForUserSerializer(
            user, data=request.data, partial=True, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSetForAdmin(ModelViewSet):
    """Работа с пользователями"""
    queryset = User.objects.all()
    serializer_class = ForAdminSerializer
    # поиск по эндпоинту users/{username}/
    lookup_field = 'username'
    permission_classes = (permissions.IsAdmin, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', )
