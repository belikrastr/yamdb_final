from django.urls import path

from .views import APIToken, APISignUp, APIUser

urlpatterns = [
    path('signup/', APISignUp.as_view(), name='signup'),
    path('token/', APIToken.as_view(), name='token'),
    path('v1/users/me/', APIUser.as_view(), name='me'),
]
