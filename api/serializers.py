from rest_framework import serializers
from users.models import User
from api.models import Post, Comment, Category


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments']


class PostCareateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", 'body', 'owner']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["post"] = PostSerializer(instance.post).data
        return data


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post', 'like', 'dislikes']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fiedls = ['id', 'title', 'body', 'owner']
