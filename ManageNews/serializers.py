# from django.contrib.auth.models import User
from datetime import datetime

from django.forms import ModelForm
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import News, Category
import time


class CategorySerializer(ModelForm):
    class Meta:
        model = Category
        fields = ['id', "name", "status"]
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        category = Category(
            name=validated_data["name"],
            status=True
        )
        category.save()
        return category

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class NewsSerializer(ModelForm):
    class Meta:
        model = News
        fields = ['id', "category_id",  "title","content", "image", "audio", "video"]

        def create(self, validated_data):
            news = News(
                category_id=validated_data['category_id'],
                title=validated_data['title'],
                content=validated_data['content'],
                image=validated_data['image'],
                audio=validated_data['audio'],
                video=validated_data["video"],
                # dateCreated=validated_data["dateCreated"],
                status=True
            )
            news.save()
            return news

        def update(self, instance, validated_data):
            return super().update(instance, validated_data)
