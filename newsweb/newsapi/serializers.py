from rest_framework import serializers
from .models import Newsletter, Article
from django.contrib.auth.models import User


class NewsletterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Newsletter
        fields = ['url', 'id', 'title', 'issue_number']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ['url', 'id', 'owner', 'newsletter', 'title', 'content']


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles']
