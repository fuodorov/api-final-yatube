from django.shortcuts import get_object_or_404
from rest_framework.serializers import (ModelSerializer, SlugRelatedField,
                                        CurrentUserDefault)
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post, User


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = ('title',)
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            )
        ]

    def validate(self, attrs):
        user = attrs.get('user')
        following = get_object_or_404(User, username=attrs.get('following'))
        if following == user:
            raise ValidationError("You can't subscribe to yourself")
        return super(FollowSerializer, self).validate(attrs)


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
