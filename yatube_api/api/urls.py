from django.urls import include, path
from rest_framework.routers import SimpleRouter


from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
]
