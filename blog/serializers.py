from rest_framework import serializers
from .models import BlogArticles


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticles
        fields = '__all__'
        lookup_fields = 'slug'