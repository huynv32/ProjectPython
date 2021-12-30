# from django.contrib.auth.models import User
from datetime import datetime

from django.forms import ModelForm
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Country, Global, Summary
import time


class CategorySerializer(ModelForm):
    class Meta:
        model = Country
        fields = ['id', "country", "slug", "countryCode"]
        # extra_kwargs = {'password': {'write_only': True}}


class QuestionSerializer(ModelForm):
    class Meta:
        model = Summary
        fields = ['id', "country", "countryCode", "confirmed", "deaths", "date"]


class AnswerSerializer(ModelForm):
    class Meta:
        model = Global
        fields = ['id', "country", "countryCode", "newConfirmed", "totalConfirmed", "newDeaths", "totalDeaths", "date"]
