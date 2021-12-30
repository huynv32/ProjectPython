# from django.contrib.auth.models import User
from datetime import datetime

import self as self
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponse
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Question, Category, Answer, Result
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


class QuestionSerializer(ModelForm):
    class Meta:
        model = Question
        fields = ['id', "category_id", "title", "image", "audio", "video"]

        def create(self, validated_data):
            question = Question(
                category_id=validated_data['category_id'],
                # user_id=validated_data['user_id'],
                title=validated_data['title'],
                image=validated_data['image'],
                audio=validated_data['audio'],
                video=validated_data["video"],
                # dateCreated=validated_data["dateCreated"],
                status=True
            )
            question.save()
            return question

        def update(self, instance, validated_data):
            return super().update(instance, validated_data)


class AnswerSerializer(ModelForm):
    class Meta:
        model = Answer
        fields = ['id', "question_id", "content", "value"]

        def create(self, validated_data):
            answer = Answer(
                question_id_id=validated_data['question_id'],
                content=validated_data["content"],
                value=validated_data["value"],
                status=True
            )
            answer.save()
            return answer

        def update(self, instance, validated_data):
            return super().update(instance, validated_data)


class ResultSerializer(ModelForm):
    class Meta:
        model = Result
        fields = ['id', "user_id", "scope", "category"]


class UserSerializer(ModelForm):
    class Meta:
        model = User
        fields = ['id', "username", "password"]
