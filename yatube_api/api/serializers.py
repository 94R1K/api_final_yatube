from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (CurrentUserDefault, ModelSerializer,
                                        ValidationError)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field='username',
                            default=CurrentUserDefault())
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Такая подписка уже существует!!!'
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise ValidationError('Неверный запрос. '
                  'Попытка подписки на себя.')
        return value
