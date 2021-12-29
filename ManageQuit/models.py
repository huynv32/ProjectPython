from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=355)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=355)
    audio = models.FileField(upload_to='audio/')
    video = models.FileField(upload_to="video/")
    image = models.FileField(upload_to='image/')
    # dateCreated = models.DateTimeField(null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=355)
    value = models.BooleanField();
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.content


class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    scope = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
