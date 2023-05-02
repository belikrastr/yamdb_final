from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)
from users.views import UserViewSetForAdmin

router = SimpleRouter()

router.register(r'titles', TitleViewSet, basename='titles')

router.register(r'categories', CategoryViewSet, basename='categories')

router.register(r'genres', GenreViewSet, basename='genres')

router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review')

router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register('users', UserViewSetForAdmin, basename='users')

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/', include(router.urls)),
]
