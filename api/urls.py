from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('follow', FollowViewSet, basename='FollowView')
v1_router.register('group', GroupViewSet, basename='GroupView')
v1_router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                   basename='CommentView')
v1_router.register('posts', PostViewSet, basename='PostView')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
