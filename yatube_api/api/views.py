from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


from posts.models import Post, Group, Follow, User
from .serializers import (
    PostSerializer, GroupSerializer,
    CommentSerializer, FollowSerializer
)
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return (ReadOnly(),)
    #     return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return (ReadOnly(),)
    #     return super().get_permissions()

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comments = post.comments.all()
        return comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following_user = get_object_or_404(
            User,
            username=self.request.data.get('following')
        )
        serializer.save(
            user=self.request.user,
            following=following_user
        )
