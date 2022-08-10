from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def create(self, validated_data):
        if self.is_valid():
            if validated_data['following'] == validated_data['user']:
                raise serializers.ValidationError('Нельзя подписаться на '
                                                  'самого себя!!!')
            if Follow.objects.filter(**validated_data).exists():
                raise serializers.ValidationError(
                    'Такая подписка уже существует!!!'
                )
        return Follow.objects.create(**validated_data)
